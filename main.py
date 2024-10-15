# instalamos e importamos la funcion de chat GPT
import openai
# importamos una funcion que contenga nuestro registro legal con GPT es decir la api key
import config
#importamos Typer para que la interaccion con GPT sea mas bonita y profesional
import typer
#desde rich importamos solo la forma que tiene de print con texto enriquecido
from rich import print
# para darle una leyenda sobre los comandos que puede utilizar en que interactua importo un tipo de tabla
from rich.table import Table


### creamos la funcion main para que esta corra a traves de typer que hemos importado e instalado como paquete, 
# el cual hace mas profesionales las interaciones con la consola
def main():
    
    openai.api_key = config.api_key
    
    # con esto aparecera en negrita y verde al principio como cabecera
    print('[bold green]ChatGPT API en Python[/bold green]')
    
    
    # creo una leyenda en una tabla con los comandos para el que interactua con la terminal
    table = Table("comando", "Descripcion")
    table.add_row('salir', 'salir de la aplixacion')
    # para comenxar una nueva conversacion y se cree de nuevo la tabla
    table.add_row('new', 'crear una nueva conversacion')
    print(table)
    
    
    ### contexto del asistente
        # system es para darle un contexto a nuestro asistente y de este modo afine su trabajo
    context = {"role": "system", 
               "content": "Eres un traductor de español a Ingles"}
    messages = [context]

    
    # para que siga formulando las preguntas usamos un while
    while true:
        ### para pasarle todo mi contenico content
        # con esto lanzara la pregunta para que interactues tu con chatgpt
        content = __prompt()

        # para poder empezar de nuevo dandole a new 
        if content == "new":
            print('Nueva conversacion')
            messages = [context]
            content = __prompt()

        
        ### para que no pierda el contexto y le pueda enviar nuevos mensajes
        # role es quien esta pasando este contenido
        # user yo soy el que le va a lanzar la pregunta a GPT
        # es un sistema de claves/valores, al igual que un json
        messages.appen({"role": "user", "content": content})



        ###llamar a OpenIA y mandarle un texto, 
        # escoger el modelo a usar y los mensajes tipo array
        # recogiendo los mensajes anteriores y teniendolos en cuenta sus respuestas a siguientes preguntas tendran en cuenta la pregunta anterior y el contexto
        response = openai.ChatCompletion.crate(model="gpt-3.5-turbo", 
                                            messages=messages)


        # me quedo con la respuesta
        # para tener una respuesta concreta a tus gustos usa choice
        # de varias respuesta que te devielva la respuesta primera[0]
        # message es lo que tienes que buscar dentro de la respuesta
        # content para buscar el contenido del mensaje
        response_content = response.choices[0].message.content


        #para que se guarde la respuesta y asi pueda seguir interactuando, y que asi tenga contexto de sus respuestas
        messages.appen({"role": "assistant", "content": response_content})


        ### imprimimos la pregunta que hemos almacenado en la variable response_content
        print(response_content)
 
 
def __promp() -> str:
    # Es un imput manejado a traves de prompt
    content = typer.prompt("\n¿sobre que quieres hablar?")
    
    if content == "salir":
        # formulario de confirmacion para asegurarnos que queremos salir
        # ademas lo guardo en una variable exit
        exit = typer.confirm('¿estas seguro de salir?')
        if exit:
            # en este caso tenemos una funcion en typer para parar la aplicacion
            # Raise para lanzar hacia arriba
            print('Hasta luego!')
            raise typer.Abort()
        # en caso de decir que no quieres salir con false usando este boleano te devuelve a la pregunta inicial
        return __prompt()
    
    return prompt
 
 
 
### creamos el if para que la funcion anterior corra a traves de typer, usando este if   
if __name__ == "__main__":
    typer.run(main)