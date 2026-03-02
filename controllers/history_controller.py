class HistoryController:
    def __init__(self, history_model):
        self.history_model = history_model

    def add_history_entry(self, entry):
        self.history_model.add_history_entry(entry)

    def get_history(self):
        return self.history_model.get_history()