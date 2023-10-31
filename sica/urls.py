from django.urls import path, include
from .views import *


# enlaces para mostrar las vistas (URLS)

urlpatternsTransaccion = [
    path('ver_transacciones', transacciones, name='transacciones'),
    path('crear_transaccion', crear_transaccion, name='crear_transaccion'),
    path('editar/<int:id_transaccion>', editar_transaccion, name='editar_transaccion'),
    path('eliminar/<int:id_transaccion>', eliminar_transaccion, name='eliminar_transaccion'),
    path('transaccion_IVA', transaccion_IVA, name='transaccion_IVA'),
    path('calculo_IVA/<int:id_transaccion>', calculo_IVA, name='calculo_IVA'),
]

urlpatterns = [
    path('', inicio, name='inicio'),
    path('catalogo', catalogo, name='catalogo'),
    path('catalogo/clase', agg_clase, name='agg_clase'),
    path('catalogo/grupo', agg_grupo, name='agg_grupo'),
    path('catalogo/cuenta', agg_cuenta, name='agg_cuenta'),
    path('catalogo/subcuenta', agg_subcuenta, name='agg_subcuenta'),
    path('catalogo/tipotrans', agg_tipotrans, name='agg_tipotrans'),
    path('catalogo/servicios', agg_servicio, name='agg_servicio'),
    path('libros', libros, name='libros'),
    

    path('mayor', mayor, name='mayor'),
    path('movimientos/<str:id_subCuenta>', movimientos, name='movimientos'),

    path('partidas', partidas, name='partidas'),
    path('partidas/crear_partida', crear_partida, name='crear_partida'),
    path('partidas/editar/<int:id_partida>', editar_partida, name='editar_partida'),
    path('partidas/eliminar/<int:id_partida>', eliminar_partida, name='eliminar_partida'),

    path('transacciones/<int:id_partida>/', include(urlpatternsTransaccion)),

    path('hojaTrabajo', hojaTrabajo, name='hojaTrabajo'),
    path('hojaTrabajo/balanceComprobacion', balanceComprobacion, name='balanceComprobacion'),

    path('hojaTrabajo/ajustes', ajustes, name='ajustes'),
    path('hojaTrabajo/ajustes/crear_ajuste', crear_ajuste, name='crear_ajuste'),
    path('hojaTrabajo/ajustes/editar/<int:id_ajuste>', editar_ajuste, name='editar_ajuste'),
    path('hojaTrabajo/ajustes/eliminar/<int:id_ajuste>', eliminar_ajuste, name='eliminar_ajuste'),

    path('hojaTrabajo/balanceComprobacionAjustado', balanceComprobacionAjustado, name='balanceComprobacionAjustado'),
    path('hojaTrabajo/estadoResultado', estadoResultado, name='estadoResultado'),
    path('hojaTrabajo/estadoCapital', estadoCapital, name='estadoCapital'),
    path('hojaTrabajo/balanceGeneral', balanceGeneral, name='balanceGeneral'),
    path('ContabilidadCostos', ContabilidadCostos, name='ContabilidadCostos'),
    path('ContabilidadCostos/OrdenProduccion.html', OrdenProduccion, name='OrdenProduccion'),
    path('ContabilidadCostos/verOrdenes.html', verOrdenes, name='verOrdenes'),
    path('ContabilidadCostos/ManodeObra.html/<int:id_OrdendeProduccion>', ManodeObraVista, name='ManodeObraVista'),
    path('ContabilidadCostos/Prorrateo.html/<int:id_OrdendeProduccion>', ProrrateoVista, name='Prorrateo'),
    path('ContabilidadCostos/verManodeObra.html/<int:id_OrdendeProduccion>', verManodeObra, name='verManodeObra'),
    path('ContabilidadCostos/verProrrateo.html/<int:id_OrdendeProduccion>', verProrrateo, name='verProrrateo'),
    path('ContabilidadCostos/CostosIndirectos.html/<int:id_OrdendeProduccion>/<int:id_Prorrateo>', CostosIndirectosView, name='CostosIndirectos'),
    path('ContabilidadCostos/verCostosIndirectos.html/<int:id_OrdendeProduccion>', verCostosIndirectos, name='verCostosIndirectos'),
    path('ContabilidadCostos/verFactura.html/<int:id_OrdendeProduccion>', verFactura, name='verFactura'),
]