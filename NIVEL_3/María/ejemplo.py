import pandas as pd
import io

def generar_resumen_por_apellido(csv_content: str) -> pd.DataFrame:
    """
    Procesa el contenido CSV, agrupa los contactos por 'Apellido', 
    y cuenta la frecuencia de cada apellido.

    Args:
        csv_content (str): Contenido completo del archivo contactos.csv.

    Returns:
        pd.DataFrame: Un DataFrame con el conteo de contactos por apellido,
                      ordenado de forma descendente.
    """
    # 1. Leer el contenido del CSV directamente desde el string
    data_io = io.StringIO(csv_content)
    df = pd.read_csv(data_io)

    # 2. Eliminar duplicados (por si acaso, aunque no es el foco principal)
    df.drop_duplicates(inplace=True)

    # 3. Agrupar por 'Apellido' y contar la ocurrencia de cada uno
    resumen_df = df.groupby('Apellido').size().reset_index(name='Total_Contactos')

    # 4. Ordenar el resumen de forma descendente por el conteo
    resumen_df = resumen_df.sort_values(by='Total_Contactos', ascending=False).reset_index(drop=True)

    return resumen_df

# Contenido del archivo contactos.csv
csv_data = """Nombre,Apellido,Correo,Teléfono
Patricia,Torres,patricia.torres@example.com,+34 685204109
Sofía,Sánchez,sofía.sánchez@example.com,+34 644949689
Carlos,Mendoza,carlos.mendoza@example.com,+34 636853872
Andrés,Jiménez,andrés.jiménez@example.com,+34 672392734
Pedro,Navarro,pedro.navarro@example.com,+34 627412759
Pedro,Gómez,pedro.gómez@example.com,+34 603361986
Sofía,Rodríguez,sofía.rodríguez@example.com,+34 684300983
Daniel,Torres,daniel.torres@example.com,+34 640456433
Pedro,Sánchez,pedro.sánchez@example.com,+34 688459642
Sofía,Morales,sofía.morales@example.com,+34 610070858
Camila,López,camila.lópez@example.com,+34 683546329
Carlos,Ramírez,carlos.ramírez@example.com,+34 646231160
Laura,Martínez,laura.martínez@example.com,+34 634700486
Jorge,López,jorge.lópez@example.com,+34 646472253
Luis,Sánchez,luis.sánchez@example.com,+34 650282206
José,Jiménez,josé.jiménez@example.com,+34 603719316
María,Sánchez,maría.sánchez@example.com,+34 678421522
Ana,Navarro,ana.navarro@example.com,+34 655237972
Laura,Pérez,laura.pérez@example.com,+34 629428339
Pedro,Rodríguez,pedro.rodríguez@example.com,+34 681183844
"""

# 1. Ejecutar la función para obtener el DataFrame resultante
resumen_contactos = generar_resumen_por_apellido(csv_data)

# 2. MODIFICACIÓN: Imprimir el DataFrame de resultados en pantalla
print("--- Resumen de Contactos Agrupados por Apellido ---")
print(resumen_contactos)