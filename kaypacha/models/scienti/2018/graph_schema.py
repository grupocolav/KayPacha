# Scienti data model 2018
# SCHEMA version for modification on the relations, it is vertioned as well
graph_schema = {"SCIENTI_MODEL": 2018}
graph_schema["MODELS"] = {}
graph_product = {"MAIN_TABLE": "EN_PRODUCTO",
                 "SCHEMA_VERSION": 0.1,
                 "GRAPH": [{"EN_PRODUCTO": [
                     # autor registrante
                     {"KEYS": ["COD_RH"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_RECURSO_HUMANO': [
                                # municipio
                                 {"KEYS": ["COD_RH_MUN_NACIM/COD_RH_MUNICIPIO", "COD_MUN_NACIM/COD_MUNICIPIO"],
                                  "DB":"__CVLAC__",
                                  "TABLES":[{'EN_MUNICIPIO': [
                                      # departamento
                                      {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                       "DB":"__CVLAC__",
                                       "TABLES":[{'EN_DEPARTAMENTO': [
                                           # pais
                                           {"KEYS": ["SGL_PAIS"],
                                            "DB":"__CVLAC__",
                                            "TABLES":[{'EN_PAIS': None}]},

                                       ]}]},
                                  ]}]},
                                 # level of studies
                                 {"KEYS": ["COD_NIVEL_FORMACION"],
                                  "DB":"__CVLAC__",
                                  "TABLES":[{'EN_NIVEL_FORMACION': None}]},
                                 ]},
                                ]},

                     # institucion registrante
                     {"KEYS": ["COD_INST_AVALA/COD_INST"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_INSTITUCION': [
                          # pais
                          {"KEYS": ["SGL_PAIS"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PAIS': None}]},

                      ]}]},
                     # Idioma
                     {"KEYS": ["SGL_IDIOMA"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_IDIOMA': None}]},

                     # Prod type
                     # Prod type level 3
                     {"KEYS": ["COD_TIPO_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_TIPO_PRODUCTO': [
                             # Prod type level 2
                             {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_TIPO_PRODUCTO': [
                                  # Prod type level 1
                                  {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_TIPO_PRODUCTO': [
                                       # Prod type level 0
                                       {"KEYS": ["COD_TIPO_PRODUCTO_PADRE/COD_TIPO_PRODUCTO"],
                                        "DB":"__CVLAC__",
                                        "TABLES":[{'EN_TIPO_PRODUCTO': None}
                                                  ]}
                                   ]}
                                  ]}

                              ]}
                             ]},

                         ]}
                     ]},
                     # Proyecto diecto de producto
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'RE_PROYECTO_PRODUCTO':
                                    [{"KEYS": ["COD_RH", "COD_PROYECTO"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[{'EN_PROYECTO': None}]},

                                     ]}]},

                     # Grupo x Producto
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__GRUPLAC__",
                      "TABLES":[{'EN_PRODUCTO_GR': [
                          # Grupo
                          {"KEYS": ["NRO_ID_GRUPO"],
                           "DB":"__GRUPLAC__",
                           "TABLES":[{"EN_GRUPO_PESQUISA": [
                               # re_institucion
                               {"KEYS": ["NRO_ID_GRUPO"],
                                "DB":"__GRUPLAC__",
                                "TABLES":[{'RE_GRUPO_INSTITUCION': [
                                    # institucion
                                    {"KEYS": ["COD_INST"],
                                     "DB":"__CVLAC__",
                                     "TABLES":[{'EN_INSTITUCION': [
                                         # pais
                                         {"KEYS": ["SGL_PAIS"],
                                          "DB":"__CVLAC__",
                                          "TABLES":[{'EN_PAIS': None}]},
                                     ]}
                                    ]}
                                ]}
                               ]},
                               # Area reconocimiento level 2 (tiene 3 niveles máximo) (es con COD_RH_AREA???)
                               {"KEYS": ['COD_RH_AREA/COD_RH', 'COD_AREA_CONHEC/COD_AREA_CONOCIMIENTO'],
                                   "DB":"__CVLAC__",
                                   "TABLES":[
                                   {"EN_AREA_CONOCIMIENTO": [
                                       # Area reconocimiento level 1
                                       {"KEYS": ['COD_RH_PADRE/COD_RH', "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO"],
                                        "DB":"__CVLAC__",
                                        "TABLES":[{'EN_AREA_CONOCIMIENTO': [
                                            # Area reconocimiento level 0
                                            {"KEYS": ['COD_RH_PADRE/COD_RH', "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_AREA_CONOCIMIENTO': None}]},
                                        ]}
                                       ]},

                                   ]}
                               ]},
                           ]},
                          ]},
                          # Proyectos pasando por grupo
                          {"KEYS": ['NRO_ID_GRUPO', 'SEQ_PRODUCTO/SEQ_PRODUCAO'],
                              "DB":"__GRUPLAC__",
                              "TABLES":[
                              {"RE_PROYECTO_PRODUCTO_GR": [{"KEYS": ["NRO_ID_GRUPO", "SEQ_PROJETO"],
                                                           "DB":"__GRUPLAC__",
                                                            "TABLES":[
                                  {"EN_PROYECTO_GR": None}
                              ]}
                              ]}
                          ]},
                      ]}
                     ]},
                     # Recurso humano otro
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'RE_PRODUCTO_RECURSO_HUM_OTRO': [{"KEYS": ["COD_RH/COD_RH_CREA", "COD_RH_OTRO"],
                                                                      "DB":"__CVLAC__",
                                                                      "TABLES":[{'EN_RECURSO_HUMANO_OTRO': None}
                                                                                ]}
                                                                     ]}
                                   ]},
                     # Prod tecnica (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_TECNICA':
                                    [{"KEYS": ["COD_RH", "COD_PRODUCTO"],
                                      "DB":"__CVLAC__",
                                      "TABLES":[
                                        # Producto Tecnilogico
                                        {'EN_PROD_TECNOLOGICO': [
                                            # Editorial
                                            {"KEYS": ["COD_EDITORIAL"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_EDITORIAL': None}]},
                                            # Editorial others
                                            {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_EDITORIAL_OTRO': None}]},

                                        ]},
                                        # secreto industrial
                                        {'EN_SECRETO_INDUSTRIAL': [
                                            # Institucion
                                            {"KEYS": ["COD_INSTITUCION/COD_INST"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_INSTITUCION': [
                                                 # pais
                                                 {"KEYS": ["SGL_PAIS"],
                                                  "DB":"__CVLAC__",
                                                  "TABLES":[{'EN_PAIS': None}]},
                                             ]}]},
                                            # Institucion otra
                                            {"KEYS": ["COD_RH", "COD_INST_OTRO/COD_INST"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_INSTITUCION_OTRA': [
                                                 # municipio
                                                 {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                                                  "DB":"__CVLAC__",
                                                  "TABLES":[{'EN_MUNICIPIO': [
                                                      # departamento
                                                      {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                                       "DB":"__CVLAC__",
                                                       "TABLES":[{'EN_DEPARTAMENTO': [
                                                           # pais
                                                           {"KEYS": ["SGL_PAIS"],
                                                            "DB":"__CVLAC__",
                                                            "TABLES":[{'EN_PAIS': None}]},

                                                       ]}]},
                                                  ]}]},

                                             ]}]},
                                        ]},
                                        # software (No tiene sub tablas)
                                        {'EN_PROD_SOFTWARE': None},
                                        # Registro
                                        {'EN_REGISTRO': [
                                            # Institucion
                                            {"KEYS": ["COD_INSTITUCION/COD_INST"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_INSTITUCION': [
                                                 # pais
                                                 {"KEYS": ["SGL_PAIS"],
                                                  "DB":"__CVLAC__",
                                                  "TABLES":[{'EN_PAIS': None}]},

                                             ]}]},
                                            # Institucion otra
                                            {"KEYS": ["COD_RH", "COD_INST_OTRO/COD_INST"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_INSTITUCION_OTRA': [
                                                 # municipio
                                                 {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                                                  "DB":"__CVLAC__",
                                                  "TABLES":[{'EN_MUNICIPIO': [
                                                      # departamento
                                                      {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                                       "DB":"__CVLAC__",
                                                       "TABLES":[{'EN_DEPARTAMENTO': [
                                                           # pais
                                                           {"KEYS": ["SGL_PAIS"],
                                                            "DB":"__CVLAC__",
                                                            "TABLES":[{'EN_PAIS': None}]},

                                                       ]}]},
                                                  ]}]},

                                             ]}]},

                                        ]},
                                        # prod vegetal (No tiene sub tablas)
                                        {'EN_PROD_VEGETAL': None},
                                        # Producto Norma
                                        {'EN_PROD_NORMA': [
                                            # Editorial
                                            {"KEYS": ["COD_EDITORIAL"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_EDITORIAL': None}]},
                                            # Editorial others
                                            {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                             "DB":"__CVLAC__",
                                             "TABLES":[{'EN_EDITORIAL_OTRO': None}]},

                                        ]},
                                        # Patente (patente es tabla primaria, no se va mas en profuncidad aca)
                                        {'EN_PATENTE': None},

                                    ]},

                                    ]}
                                   ]},
                     # Prod artistica (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_ARTISTICA': [
                          # prod artistica detalles
                          {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PROD_ARTISTICA_DETALLE': None}
                                     ]},
                          # Area reconocimiento level 2 (tiene 3 niveles máximo)
                          {"KEYS": ['COD_RH_AREA_CON/COD_RH', 'COD_AREA_CONOCIMIENTO'],
                           "DB":"__CVLAC__",
                           "TABLES":[
                               {"EN_AREA_CONOCIMIENTO": [
                                   # Area reconocimiento level 1
                                   {"KEYS": ['COD_RH_PADRE/COD_RH', "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO"],
                                    "DB":"__CVLAC__",
                                    "TABLES":[{'EN_AREA_CONOCIMIENTO': [
                                        # Area reconocimiento level 0
                                        {"KEYS": ['COD_RH_PADRE/COD_RH', "COD_AREA_PADRE/COD_AREA_CONOCIMIENTO"],
                                         "DB":"__CVLAC__",
                                         "TABLES":[{'EN_AREA_CONOCIMIENTO': None}]},
                                    ]}
                                   ]},

                               ]}
                          ]},
                      ]}
                     ]},
                     # Tesis orientada (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_TESIS_ORIENTADA': [
                          # Programa academico
                          {"KEYS": ["COD_RH_PROGRAMA/COD_RH", "COD_PROGRAMA_ACADEMICO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PROGRAMA_ACADEMICO': None}]},
                          # Institucion (HAY DOS OPCIONES ACA! COD_INST y CON_INSTITUCION)cual??
                          {"KEYS": ["COD_INST"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_INSTITUCION': [
                               # pais
                               {"KEYS": ["SGL_PAIS"],
                                "DB":"__CVLAC__",
                                "TABLES":[{'EN_PAIS': None}]},

                           ]}]},


                      ]}]},
                     # Producion audiovisual (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_AUDIOVISUAL': [
                             # municipio
                             {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_MUNICIPIO': [
                                  # departamento
                                  {"KEYS": ["SGL_PAIS", "SGL_DEPARTAMENTO"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_DEPARTAMENTO': [
                                       # pais
                                       {"KEYS": ["SGL_PAIS"],
                                        "DB":"__CVLAC__",
                                        "TABLES":[{'EN_PAIS': None}]},

                                   ]}]},
                              ]}]},


                         ]}]},
                     # Partitura (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_PARTITURA': [
                             # Editorial
                             {"KEYS": ["COD_EDITORIAL"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_EDITORIAL': None}]},
                             # Editorial others
                             {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_EDITORIAL_OTRO': None}]},
                         ]}]},
                     # Capitulo libro (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_CAPITULO_LIBRO': None}]},
                     # libro (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_LIBRO': None}]},
                     # Cursos (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_CURSO': None}]},
                     # capitulo de momoria (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_CAP_MEMORIA': None}]},

                     # Prod Articulos (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                         "DB":"__CVLAC__",
                         "TABLES":[{'EN_PROD_ARTICULO': [
                             # revista
                             {"KEYS": ["COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA': [
                                  # editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]}
                              ]}
                             ]},
                             # revista otra
                             {"KEYS": ["COD_RH", "COD_REVISTA_OTRO/COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA_OTRA': [
                                  # Editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]},
                                  # Editorial otro
                                  {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL_OTRO': None}
                                             ]},
                              ]}
                             ]},
                         ]}
                     ]},
                     # Prod biblio (Details)
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_PROD_BIBLIO': [
                          # revista
                          {"KEYS": ["COD_REVISTA"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_REVISTA': [
                               # editorial
                               {"KEYS": ["COD_EDITORIAL"],
                                "DB":"__CVLAC__",
                                "TABLES":[{'EN_EDITORIAL': None}
                                          ]}
                           ]}
                          ]},
                          # revista otra
                          {"KEYS": ["COD_RH", "COD_REVISTA_OTRO/COD_REVISTA"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_REVISTA_OTRA': [
                                  # Editorial
                                  {"KEYS": ["COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL': None}
                                             ]},
                                  # Editorial otro
                                  {"KEYS": ["COD_RH", "COD_EDITORIAL_OTRO/COD_EDITORIAL"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_EDITORIAL_OTRO': None}
                                             ]},
                              ]}
                          ]},
                      ]}
                     ]},
                     # Re-Sector Apliación
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PRODUCTO_SECTOR_APL': [
                          # sector aplicación nivel 2
                          {"KEYS": ["COD_SECTOR_APLICACION"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_SECTOR_APLICACION': [
                               # sector aplicación nivel 1
                               {"KEYS": ["COD_SECT_APLIC_PADRE/COD_SECTOR_APLICACION"],
                                "DB":"__CVLAC__",
                                "TABLES":[{'EN_SECTOR_APLICACION': None}
                                          ]}
                           ]}
                          ]}
                      ]}

                     ]},
                     # Re-Palabra clave
                     {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_PRODUCTO_PALABRA_CLA': [
                          # Palabra clave
                          {"KEYS": ["COD_RH", "COD_PALABRA_CLAVE"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_PALABRA_CLAVE': None}
                                     ]}
                      ]}

                     ]}
                 ]}
                 ]}


# RE_PROYECTO_RED está vacia, no se pueden obtener los proyectos por acá
graph_network = {"MAIN_TABLE": "EN_RED",
                 "SCHEMA_VERSION": 0.1,
                 "GRAPH": [{"EN_RED": [
                     # autor registrante
                     {"KEYS": ["COD_RH"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_RECURSO_HUMANO': None}]},

                     # institucion registrante
                     {"KEYS": ["COD_INST_AVALA/COD_INST"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'EN_INSTITUCION': None}]},
                     # Re-Institucion
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_INSTITUCION_RED': [
                          # instituciones
                          {"KEYS": ["COD_RH", "COD_INSTITUCION/COD_INST"],
                              "DB":"__CVLAC__",
                              "TABLES":[{'EN_INSTITUCION_OTRA': None}
                                        ]}
                      ]}
                     ]},
                     # Re-Autor otros
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_RH_O_RED': [
                          # Autores otros
                          {"KEYS": ["COD_RH/COD_RH_CREA", "COD_RH_OTRO"],
                           "DB":"__CVLAC__",
                           "TABLES":[{'EN_RECURSO_HUMANO_OTRO': None}
                                     ]}

                      ]}

                     ]},
                     # Re-Comunidad
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__CVLAC__",
                      "TABLES":[{'RE_RED_COMUNIDAD':
                                 # Comunidad
                                 [{"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                   "DB":"__CVLAC__",
                                   "TABLES":[{'EN_COMUNIDAD': [
                                       # Municipio
                                       {"KEYS": ["COD_RH_MUNICIPIO", "COD_MUNICIPIO"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'EN_MUNICIPIO': None}]},
                                       # Re-proyecto comunidad
                                       {"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'RE_PROYECTO_COMUNIDAD': [
                                               # proyecto
                                               {"KEYS": ["COD_RH", "COD_PROYECTO"],
                                                "DB":"__CVLAC__",
                                                "TABLES":[{"EN_PROYECTO": None}]}
                                           ]}]},
                                       # Re-producto comunidad
                                       {"KEYS": ["COD_RH", "COD_COMUNIDAD"],
                                           "DB":"__CVLAC__",
                                           "TABLES":[{'RE_PRODUCTO_COMUNIDAD': [
                                               # producto
                                               {"KEYS": ["COD_RH", "COD_PRODUCTO"],
                                                "DB":"__CVLAC__",
                                                "TABLES":[{"EN_PRODUCTO": None}]}
                                           ]}]},

                                   ]}
                                 ]},

                                 ]}
                                ]},

                     # Re-Grupo
                     {"KEYS": ["COD_RH", "COD_RED"],
                      "DB":"__GRUPLAC__",
                      "TABLES":[{'RE_GRUPO_RH_RED': [
                          # Grupo
                          {"KEYS": ["NRO_ID_GRUPO"],
                           "DB":"__GRUPLAC__",
                           "TABLES":[{"EN_GRUPO_PESQUISA": [
                               # re_institucion
                               {"KEYS": ["NRO_ID_GRUPO"],
                                "DB":"__GRUPLAC__",
                                "TABLES":[{'RE_GRUPO_INSTITUCION': [
                                    # institucion
                                    {"KEYS": ["COD_INST"],
                                     "DB":"__CVLAC__",
                                     "TABLES":[{'EN_INSTITUCION': None}
                                               ]}
                                ]}
                               ]},
                               # Area reconocimiento
                               {"KEYS": ['COD_AREA_CONHEC/COD_AREA_CONOCIMIENTO'],
                                "DB":"__CVLAC__",
                                "TABLES":[
                                   {"EN_AREA_CONOCIMIENTO": None}
                               ]},

                           ]},
                          ]}
                      ]}

                     ]},

                 ]}
                 ]}


graph_schema["MODELS"]["network"] = graph_network
graph_schema["MODELS"]["product"] = graph_product
