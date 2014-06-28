ON_QUERY = {
    "dimreferenciasdw": "ON r.idReferencia = f.idReferencia",
    "dimunidadclientedw": "ON c.UNI_CODIGO = f.UNI_CODIGODW",
    "tiempo": "ON t.id_date = f.ref_date_id"
}

DIM_SCUT = {
    "dimreferenciasdw": "r",
    "dimunidadclientedw": "c",
    "tiempo": "t"
}

HIER_ORDER = ['Anho', 'Mes', 'Dia', 'sDpto', 'sProv', 'sDist',
              'CLI_NOMBRE', 'UNI_MATRICULA']
