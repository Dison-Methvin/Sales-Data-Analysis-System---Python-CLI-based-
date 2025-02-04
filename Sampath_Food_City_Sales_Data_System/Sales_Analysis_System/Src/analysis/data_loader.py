import pandas as pd

class DataLoader:
    _instance = None
    _observers = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def load_data(file_path):
        try:
            if file_path.endswith('.xlsx'):
                # Loaded the dataset from the specified Excel file path
                df = pd.read_excel(file_path)
            elif file_path.endswith('.csv'):
                # Loaded the dataset from the specified CSV file path
                df = pd.read_csv(file_path)
            else:
                raise ValueError("Unsupported file format. Please use .xlsx or .csv files.")
            print("Dataset loaded successfully.")
            DataLoader.notify_observers(df)
            return df
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def add_observer(observer):
        DataLoader._observers.append(observer)

    @staticmethod
    def notify_observers(df):
        for observer in DataLoader._observers:
            observer.update(df)

class DataObserver:
    def update(self, df):
        raise NotImplementedError("Subclasses should implement this method.")
