from conexion import Conexion
from parametros_fisiologicos import ParametrosFisiologicos
class CondicionesMedicas:
    def __init__(self, id_condicion_medica = 0, descripcion = "", parametros = []):
        self.id_condicion_medica = id_condicion_medica
        self.descripcion = descripcion
        self.parametros = parametros
        self.cargar_parametros()
    
    def obtener_lista_condiciones_medicas(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Condiciones_Medicas")
        return resultado
    
    def cargar_parametros(self):
        bd = Conexion()
        resultado = bd.execute_query(
            "SELECT P.id_parametro_fisiologico, P.descripcion, P.min_estandar, P.max_estandar, P.alerta_bajo, P.alerta_alto, P.critico_bajo, P.critico_alto, P.instrucciones " +
            "FROM Condicion_Parametro as CP " +
            "INNER JOIN Parametros_Fisiologicos P  ON CP.id_parametro_fisiologico = P.id_parametro_fisiologico " +
            "WHERE CP.id_condicion_medica = ?", [self.id_condicion_medica])
        if resultado:
            for parametro in resultado:
                p = ParametrosFisiologicos(parametro[0], parametro[1], parametro[2], parametro[3], parametro[4], parametro[5], parametro[6], parametro[7], parametro[8])
                self.parametros.append(p)
    
#prueba = CondicionesMedicas()
#print(prueba.obtener_lista_condiciones_medicas())