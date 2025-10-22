
import pandas as pd
from typing import Union

def limpiar_datos_nulos_y_duplicados(
    df: pd.DataFrame,
    reset_index: bool = True
) -> pd.DataFrame:
    """
    Limpia un DataFrame de Pandas eliminando:
    1. Todas las filas que contengan al menos un valor nulo (NaN).
    2. Todas las filas que sean duplicados exactos.

    Args:
        df (pd.DataFrame): El DataFrame de entrada a limpiar.
        reset_index (bool): Si es True, el índice del DataFrame resultante
                             se restablece (0, 1, 2, ...). Por defecto es True.

    Returns:
        pd.DataFrame: El DataFrame limpio.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("La entrada debe ser un objeto pd.DataFrame.")

    # 1. Eliminar filas con valores nulos (NaN)
    # 'dropna()' elimina filas donde exista CUALQUIER valor NaN.
    df_sin_nulos = df.dropna(how='any')

    # 2. Eliminar filas duplicadas
    # 'drop_duplicates()' elimina filas que son exactamente iguales a una anterior.
    df_limpio = df_sin_nulos.drop_duplicates()

    # 3. Restablecer el índice si se solicita
    if reset_index:
        df_limpio = df_limpio.reset_index(drop=True)

    print(f"✔️ Limpieza completada.")
    print(f"   - Filas originales: {len(df)}")
    print(f"   - Filas finales: {len(df_limpio)}")

    return df_limpio

# --- Ejemplo de Uso ---
if __name__ == '__main__':
    # Creación de un DataFrame de ejemplo con nulos y duplicados
    datos_ejemplo = {
        'ID': [1, 2, 3, 4, 4, 5, 6, 7],
        'Valor': [100, 200, None, 400, 400, 500, 600, 700],
        'Categoria': ['A', 'B', 'C', 'D', 'D', 'E', None, 'F'],
        'Check': [True, False, True, False, False, True, False, True]
    }
    df_sucio = pd.DataFrame(datos_ejemplo)

    print("--- DataFrame Original ---")
    print(df_sucio)
    print("-" * 30)

    # Llamada a la función de limpieza
    df_purificado = limpiar_datos_nulos_y_duplicados(df_sucio)

    print("\n--- DataFrame Limpio ---")
    print(df_purificado)