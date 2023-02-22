import typing as tp

import torch
from transformers import BertForSequenceClassification, BertTokenizerFast


class NftScamModel:
    def __init__(self, model_path: str, device="cpu"):
        self.device = torch.device(device)

        self.bert = BertForSequenceClassification.from_pretrained(model_path).eval().to(self.device)
        self.tokenizer = BertTokenizerFast.from_pretrained(model_path)

    @torch.no_grad()
    def predict_logits(self, data: tp.List[str]) -> torch.Tensor:
        inputs = self.tokenize(data)
        inputs = self.inputs_to_device(inputs)
        output = self.bert(**inputs)
        return output.logits

    def classify(self, data: tp.List[str]) -> tp.List[int]:
        logits = self.predict_logits(data)
        classes = torch.argmax(logits, dim=1)
        classes = classes.cpu().tolist()

        return classes

    def check_scam(self, data: tp.List[str]) -> tp.List[bool]:
        classes = self.classify(data)
        return [bool(1 - c) for c in classes]

    def tokenize(self, data: tp.List[str]):
        inputs = self.tokenizer(
            data,
            add_special_tokens=True,
            padding=True,
            truncation=True,
            max_length=256,
            return_tensors="pt"
        )

        return inputs

    def inputs_to_device(
            self,
            inputs: tp.Dict[str, torch.Tensor]
    ) -> tp.Dict[str, torch.Tensor]:
        return {key: tensor.to(self.device) for key, tensor in inputs.items()}


__all__ = [
    "NftScamModel"
]
