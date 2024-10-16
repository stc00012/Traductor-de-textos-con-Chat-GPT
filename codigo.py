
import openai
import config
import typer
from rich import print
from rich.table import Table

def main():
    
    openai.api_key = config.api_key
    print('[bold green]ChatGPT API en Python[/bold green]')

    table = Table("comando", "Descripcion")
    table.add_row('salir', 'salir de la aplixacion')
    table.add_row('new', 'crear una nueva conversacion')
    print(table)
    
    context = {"role": "system", 
               "content": "Eres un traductor de español a Ingles"}
    messages = [context]

    while true:
        content = __prompt()
        
        if content == "new":
            print('Nueva conversacion')
            messages = [context]
            content = __prompt()
            
        messages.appen({"role": "user", "content": content})
        
        response = openai.ChatCompletion.crate(model="gpt-3.5-turbo", 
                                               messages=messages)
        
        response_content = response.choices[0].message.content
        
        messages.appen({"role": "assistant", "content": response_content})
        
        print(response_content)
 
 
def __prompt() -> str:
    prompt = typer.prompt("\n¿sobre que quieres hablar?")
    
    if prompt == "salir":
        exit = typer.confirm('¿estas seguro de salir?')
        if exit:
            print('Hasta luego!')
            raise typer.Abort()
        return __prompt()
    
    return prompt
  
if __name__ == "__main__":
    typer.run(main)