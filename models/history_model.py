class HistoryModel:
    def __init__(self, history_service):
        self.history_service = history_service

    def add_history_entry(self, entry):
        self.history_service.add_entry(entry)

    def get_history(self):
        return self.history_service.get_history()