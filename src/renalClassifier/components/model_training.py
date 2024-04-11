import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import matplotlib.pyplot as plt
import time
import pandas as pd
from pathlib import Path
from src.renalClassifier.entity.config_entity import TrainigConfig

class Training:
    def __init__(self, config: TrainigConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )


    @staticmethod
    def save_model(path: Path, model: tf.keras.models.Model):
        model.save(path)

    def train(self):
        self.model.compile(
            loss = 'categorical_crossentropy',
            optimizer = 'adam',
            metrics = ['accuracy']
        )

        self.history = self.model.fit(
            self.train_generator,
            steps_per_epoch = self.train_generator.n // self.train_generator.batch_size,
            epochs = self.config.params_epochs,
            validation_data = self.valid_generator,
            validation_steps = self.valid_generator.n // self.valid_generator.batch_size
        )

        self.model_metrics = self.model.evaluate(
            self.valid_generator,
            steps = self.valid_generator.n // self.valid_generator.batch_size
        )

        self.save_model(
            path = self.config.trained_model_path, 
            model = self.model
            )
