from utils import Inference

class InferenceController(Inference):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        if len(self.ui.modelComboBox.currentText()) > 0:
            self.model = self.ui.modelComboBox.currentText()
            net = self.create(self.model)
        else:
            self.model = None

        # Slot connection
        self.ui.modelComboBox.activated.connect(self.update_model)

    def update_model(self):
        self.model = self.ui.modelComboBox.currentText()
        net = self.create(self.model)