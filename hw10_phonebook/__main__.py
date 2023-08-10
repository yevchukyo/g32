from hw10_phonebook.controller import PhonebookController
import typer
from hw10_phonebook import DATABASE_PATH, __app_name__

app = typer.Typer()

@app.command()
def main():
    data_file = f'{DATABASE_PATH}/{__app_name__}.ini'
    controller = PhonebookController(data_file)
    controller.run()

if __name__ == "__main__":
    app()



