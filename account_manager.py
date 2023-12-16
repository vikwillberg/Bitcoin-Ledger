import json

class AccountManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.nicknames = self._load_nicknames()

    def _load_nicknames(self):
        try:
            with open(self.config_file, 'r') as file:
                file_content = file.read()
                print(f"Contents of {self.config_file}:\n{file_content}")
                file.seek(0)
                return json.load(file)
        except json.JSONDecodeError as json_err:
            print(f"JSON parsing error in {self.config_file}: {json_err}")
            return {}
        except FileNotFoundError:
            print(f"Config file '{self.config_file}' not found. Continuing without nickname substitution.")
            return {}

    def get_nickname(self, account_number):
        return self.nicknames.get(account_number, account_number)
        
