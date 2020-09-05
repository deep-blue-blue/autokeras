# Copyright 2020 The AutoKeras Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from autokeras import preprocessors
from autokeras.engine import hyper_preprocessor


class DefaultHyperPreprocessor(hyper_preprocessor.HyperPreprocessor):
    """HyperPreprocessor without hp usage."""

    def __init__(self, preprocessor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preprocessor = preprocessor

    def build(self, hp, dataset):
        return self.preprocessor

    def get_config(self):
        config = super().get_config()
        config.update({"preprocessor": preprocessors.serialize(self.preprocessor)})
        return config

    @classmethod
    def from_config(cls, config):
        config["preprocessor"] = preprocessors.deserialize(config["preprocessor"])
        return super().from_config(config)