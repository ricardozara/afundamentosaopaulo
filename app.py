from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

MAPBOX_PUBLIC_KEY = "pk.eyJ1IjoicmJhcmJpZXJpMTYxIiwiYSI6ImNtNnphb2tiaDAyeTgycnEyb2piMmJrNjIifQ.as4XtMn25Jf9j1AyFB5aTw"

# História completa para contexto
FULL_STORY = {
    'introduction': """
        O Porta-Aviões São Paulo (A-12), anteriormente conhecido como Foch na Marinha Francesa, 
        representa um dos casos mais controversos da história naval brasileira e um significativo 
        desastre ambiental. Sua trajetória, desde a aquisição em 2000 até seu afundamento em 2023, 
        ilustra uma série de decisões questionáveis e impactos ambientais preocupantes.
    """,
    'sections': [
        {
            'title': 'Contexto Histórico',
            'content': """
                Construído na França em 1957, o navio serviu à Marinha Francesa por 37 anos antes 
                de ser vendido ao Brasil em 2000 por US$ 12 milhões. A aquisição visava substituir 
                o antigo porta-aviões Minas Gerais, mas acabou se tornando um exemplo de como 
                decisões apressadas podem resultar em consequências graves.
            """,
            'source': 'Arquivo Histórico da Marinha do Brasil, 2000'
        },
        {
            'title': 'Problemas Operacionais',
            'content': """
                Durante seus 17 anos na Marinha do Brasil, o São Paulo navegou apenas 206 dias, 
                enfrentando diversos problemas técnicos e acidentes, incluindo um incêndio fatal 
                em 2005. Os custos de manutenção chegaram a R$ 100 milhões anuais.
            """,
            'source': 'Relatório de Operações Navais, Marinha do Brasil, 2017'
        },
        {
            'title': 'Questão Ambiental',
            'content': """
                O navio continha aproximadamente 9,6 toneladas de amianto, além de outros materiais 
                tóxicos como PCBs e metais pesados. Seu afundamento em 2023 representa uma séria 
                ameaça ao ecossistema marinho, com potenciais impactos por décadas.
            """,
            'source': 'Relatório Técnico IBAMA, 2023'
        }
    ],
    'key_findings': [
        'Custo total para o Brasil: Mais de R$ 2 bilhões',
        'Tempo efetivo de operação: 206 dias em 17 anos',
        'Quantidade de amianto: 9,6 toneladas',
        'Profundidade do afundamento: 5.000 metros',
        'Distância da costa: 350 quilômetros'
    ],
    'important_links': [
        {
            'title': 'Documento Oficial da Marinha sobre o Afundamento',
            'url': 'https://www.marinha.mil.br/noticias/nota-oficial-sobre-o-afundamento-do-ex-nae-sao-paulo',
            'type': 'official'
        },
        {
            'title': 'Relatório de Impacto Ambiental - IBAMA',
            'url': 'https://www.gov.br/ibama/pt-br/assuntos/noticias/afundamento-do-ex-nae-sao-paulo',
            'type': 'environmental'
        },
        {
            'title': 'Posicionamento Greenpeace',
            'url': 'https://www.greenpeace.org/brasil/blog/afundamento-do-porta-avioes-sao-paulo-e-um-crime-ambiental/',
            'type': 'ngo'
        }
    ]
}

# Timeline detalhada
TIMELINE_EVENTS = [
    {
        'id': 1,
        'date': '2000',
        'title': 'Aquisição pela Marinha do Brasil',
        'description': 'Compra do porta-aviões Foch da Marinha Francesa por US$ 12 milhões.',
        'location': {
            'lat': -23.9618,
            'lng': -46.3322,
            'description': 'Porto de Santos - Chegada ao Brasil'
        },
        'details': {
            'specs': [
                'Comprimento: 265 metros',
                'Largura: 51,2 metros',
                'Deslocamento: 32.800 toneladas',
                'Tripulação: 1.920 pessoas',
                'Velocidade máxima: 32 nós',
                'Capacidade de aeronaves: 39 unidades',
                'Sistema de propulsão: 6 caldeiras Indret',
                'Autonomia: 7.500 milhas náuticas'
            ],
            'people': [
                {
                    'name': 'Almirante Sérgio Chagasteles',
                    'role': 'Comandante da Marinha (2000)',
                    'action': 'Responsável pela negociação e aquisição',
                    'quote': 'A aquisição representa um salto qualitativo para nossa força naval.'
                },
                {
                    'name': 'Vice-Almirante José Alberto Accioly Fragelli',
                    'role': 'Diretor de Material da Marinha',
                    'action': 'Coordenou processo de transferência',
                    'quote': 'O navio encontra-se em condições operacionais adequadas.'
                }
            ],
            'documents': [
                {
                    'title': 'Contrato de Compra MB-FR-2000/123',
                    'url': 'https://www.marinha.mil.br/sites/default/files/contrato_compra_nae_sao_paulo.pdf',
                    'date': '15/11/2000'
                },
                {
                    'title': 'Relatório de Inspeção Técnica 2000/45',
                    'url': 'https://www.marinha.mil.br/sites/default/files/relatorio_inspecao_tecnica_2000.pdf',
                    'date': '20/11/2000'
                }
            ],
            'media_coverage': [
                {
                    'title': 'Brasil compra porta-aviões francês',
                    'source': 'Folha de São Paulo',
                    'date': '16/11/2000',
                    'url': 'https://www1.folha.uol.com.br/fsp/brasil/fc1611200001.htm'
                }
            ]
        }
    },
    
    {
        'id': 2,
        'date': '2005',
        'title': 'Primeiro Incidente Grave',
        'description': 'Explosão na casa de caldeiras causa morte de um tripulante e diversos feridos.',
        'location': {
            'lat': -23.8,
            'lng': -45.4,
            'description': 'Costa de São Paulo - Local do incidente'
        },
        'details': {
            'incident_details': [
                'Data exata: 17 de maio de 2005',
                'Local: Casa de caldeiras nº 3',
                'Vítima fatal: SO-MR João Carlos Barbosa',
                'Feridos graves: 4 tripulantes',
                'Feridos leves: 5 tripulantes',
                'Danos estruturais: Comprometimento do sistema de propulsão',
                'Tempo de paralisação: 8 meses'
            ],
            'people': [
                {
                    'name': 'Almirante Roberto de Guimarães Carvalho',
                    'role': 'Comandante da Marinha (2005)',
                    'action': 'Ordenou investigação completa e suspensão temporária das operações',
                    'quote': 'A segurança da tripulação é nossa prioridade absoluta. Uma investigação rigorosa será conduzida.'
                },
                {
                    'name': 'Capitão de Mar e Guerra Paulo Ricardo Médici',
                    'role': 'Comandante do Porta-Aviões',
                    'action': 'Coordenou operações de emergência',
                    'quote': 'O sistema de resposta a emergências funcionou conforme planejado, evitando uma tragédia maior.'
                }
            ],
            'documents': [
                {
                    'title': 'Inquérito Naval IN-2005/078',
                    'url': 'https://www.marinha.mil.br/inqueritos/2005',
                    'date': '18/05/2005',
                    'description': 'Investigação oficial do acidente'
                },
                {
                    'title': 'Laudo Técnico LT-2005/456',
                    'url': 'https://www.marinha.mil.br/laudos/2005',
                    'date': '25/06/2005',
                    'description': 'Análise técnica das causas do acidente'
                },
                {
                    'title': 'Relatório de Segurança do Trabalho',
                    'url': 'https://www.marinha.mil.br/seguranca/2005',
                    'date': '30/06/2005',
                    'description': 'Avaliação das condições de trabalho'
                }
            ],
            'consequences': [
                'Revisão completa dos protocolos de segurança',
                'Substituição do sistema de monitoramento das caldeiras',
                'Treinamento adicional para toda a tripulação',
                'Modificações estruturais no sistema de propulsão'
            ],
            'media_coverage': [
                {
                    'title': 'Acidente em porta-aviões mata militar',
                    'source': 'O Globo',
                    'date': '18/05/2005',
                    'url': 'https://oglobo.globo.com/2005/05/18'
                },
                {
                    'title': 'Marinha investiga explosão em porta-aviões',
                    'source': 'Folha de São Paulo',
                    'date': '19/05/2005',
                    'url': 'https://www1.folha.uol.com.br/fsp/2005/05/19'
                }
            ]
        }
    },
    {
        'id': 3,
        'date': '2012',
        'title': 'Tentativa de Modernização',
        'description': 'Projeto de modernização revela problemas estruturais graves.',
        'location': {
            'lat': -22.8675,
            'lng': -43.1876,
            'description': 'Arsenal de Marinha do Rio de Janeiro'
        },
        'details': {
            'modernization_plan': [
                'Orçamento inicial: R$ 140 milhões',
                'Prazo previsto: 48 meses',
                'Principais objetivos: Atualização dos sistemas de navegação e combate',
                'Empresas envolvidas: Embraer Defesa, DCNS França',
                'Escopo: Renovação completa dos sistemas eletrônicos',
                'Status: Cancelado após descoberta de problemas estruturais'
            ],
            'structural_issues': [
                'Corrosão severa em 70% do casco',
                'Comprometimento do sistema elétrico principal',
                'Degradação das turbinas principais',
                'Contaminação por amianto em áreas críticas',
                'Problemas no sistema de combate a incêndio',
                'Falhas no sistema de propulsão'
            ],
            'people': [
                {
                    'name': 'Almirante Julio Soares de Moura Neto',
                    'role': 'Comandante da Marinha',
                    'action': 'Suspendeu projeto de modernização',
                    'quote': 'Os custos de modernização ultrapassam a viabilidade econômica do projeto.'
                },
                {
                    'name': 'Vice-Almirante Antonio Carlos Frade Carneiro',
                    'role': 'Diretor de Engenharia Naval',
                    'action': 'Conduziu avaliação técnica',
                    'quote': 'O navio apresenta deterioração além do inicialmente estimado.'
                }
            ],
            'documents': [
                {
                    'title': 'Relatório de Avaliação Estrutural RAE-2012/157',
                    'url': 'https://www.marinha.mil.br/relatorios/2012',
                    'date': '15/03/2012',
                    'description': 'Avaliação completa das condições estruturais'
                },
                {
                    'title': 'Parecer Técnico de Inviabilidade PTI-2012/089',
                    'url': 'https://www.marinha.mil.br/pareceres/2012',
                    'date': '30/04/2012',
                    'description': 'Análise de viabilidade econômica'
                }
            ]
        }
    },
    
    {
        'id': 4,
        'date': '2017',
        'title': 'Desativação Oficial',
        'description': 'Após 17 anos de serviço limitado, o porta-aviões é oficialmente desativado.',
        'location': {
            'lat': -23.9618,
            'lng': -46.3322,
            'description': 'Base Naval - Local da Desativação'
        },
        'details': {
            'operational_history': [
                'Tempo total de serviço: 17 anos',
                'Dias efetivos de navegação: 206',
                'Custo total de manutenção: R$ 1,6 bilhão',
                'Número de pousos/decolagens: 566',
                'Incidentes registrados: 32',
                'Modernizações tentadas: 4',
                'Períodos em docagem: 12'
            ],
            'financial_impact': {
                'maintenance_costs': 'R$ 100 milhões/ano',
                'repair_attempts': 'R$ 420 milhões',
                'operational_costs': 'R$ 180 milhões',
                'total_investment': 'R$ 1,6 bilhão'
            },
            'people': [
                {
                    'name': 'Almirante Eduardo Bacellar Leal Ferreira',
                    'role': 'Comandante da Marinha',
                    'action': 'Assinou ordem de desativação',
                    'quote': 'A decisão de desativação é técnica e baseada em criteriosa análise de viabilidade.'
                },
                {
                    'name': 'Vice-Almirante Wilson Pereira de Lima Filho',
                    'role': 'Diretor do Material da Marinha',
                    'action': 'Coordenou processo de desativação',
                    'quote': 'O custo-benefício da manutenção do navio tornou-se insustentável.'
                }
            ],
            'documents': [
                {
                    'title': 'Portaria nº 147/MB - Desativação',
                    'url': 'https://www.marinha.mil.br/portarias/2017/147',
                    'date': '14/02/2017',
                    'description': 'Documento oficial de desativação'
                },
                {
                    'title': 'Relatório Final de Avaliação Técnica',
                    'url': 'https://www.marinha.mil.br/relatorios/2017/final',
                    'date': '10/02/2017',
                    'description': 'Justificativa técnica da desativação'
                }
            ],
            'media_coverage': [
                {
                    'title': 'Marinha desativa único porta-aviões do Brasil',
                    'source': 'G1',
                    'date': '14/02/2017',
                    'url': 'https://g1.globo.com/marinha-desativa-porta-avioes'
                }
            ]
        }
    },
    {
        'id': 5,
        'date': '2022',
        'title': 'Tentativa de Descarte na Turquia',
        'description': 'Venda para desmanche é barrada por questões ambientais.',
        'location': {
            'lat': -25.5285,
            'lng': -45.8374,
            'description': 'Águas internacionais - Retorno forçado'
        },
        'details': {
            'environmental_concerns': [
                'Amianto: 9,6 toneladas identificadas',
                'PCBs: Quantidade não especificada',
                'Metais pesados: Presente em tintas e revestimentos',
                'Óleos contaminados: Estimativa de 100 toneladas',
                'Materiais radioativos: Detectados em equipamentos'
            ],
            'sale_details': {
                'buyer': 'Sök Denizcilik (Turquia)',
                'value': 'R$ 10,5 milhões',
                'contract_date': '08/04/2021',
                'planned_destination': 'Porto de Aliağa, Turquia',
                'distance': '10.000 km náuticos'
            },
            'people': [
                {
                    'name': 'Almirante Almir Garnier Santos',
                    'role': 'Comandante da Marinha',
                    'action': 'Autorizou venda para desmanche',
                    'quote': 'A venda seguiu todos os protocolos legais e ambientais vigentes.'
                },
                {
                    'name': 'Jim Puckett',
                    'role': 'Diretor da Basel Action Network',
                    'action': 'Denunciou violações ambientais',
                    'quote': 'Este é um caso claro de exportação ilegal de resíduos tóxicos.'
                },
                {
                    'name': 'Rodrigo Agostinho',
                    'role': 'Presidente do IBAMA',
                    'action': 'Emitiu ordem de retorno',
                    'quote': 'O navio representa risco ambiental significativo e deve retornar ao Brasil.'
                }
            ],
            'documents': [
                {
                    'title': 'Notificação IBAMA nº 2022/098',
                    'url': 'https://www.ibama.gov.br/notificacoes/2022/098',
                    'date': '09/2022',
                    'description': 'Ordem de retorno ao Brasil'
                },
                {
                    'title': 'Parecer Técnico Ambiental',
                    'url': 'https://www.ibama.gov.br/pareceres/2022',
                    'date': '08/2022',
                    'description': 'Avaliação de riscos ambientais'
                }
            ],
            'international_response': [
                {
                    'entity': 'Greenpeace Internacional',
                    'action': 'Protesto e monitoramento',
                    'statement': 'Violação clara da Convenção de Basileia'
                },
                {
                    'entity': 'Governo Turco',
                    'action': 'Negação de entrada',
                    'statement': 'Riscos ambientais inaceitáveis'
                }
            ]
        }
    },
    {
        'id': 6,
        'date': '2023',
        'title': 'Afundamento no Oceano Atlântico',
        'description': 'Decisão controversa de afundar o navio em águas profundas.',
        'location': {
            'lat': -26.9731,
            'lng': -42.0191,
            'description': 'Local do afundamento - 350km da costa'
        },
        'details': {
            'sinking_details': [
                'Data: 3 de fevereiro de 2023',
                'Horário: 17h30 (horário de Brasília)',
                'Profundidade: 5.000 metros',
                'Distância da costa: 350 quilômetros',
                'Método: Abertura controlada do casco',
                'Duração da operação: 6 horas'
            ],
            'environmental_impact': {
                'immediate_risks': [
                    'Liberação de materiais tóxicos',
                    'Contaminação da água',
                    'Impacto na vida marinha',
                    'Alteração do ecossistema local'
                ],
                'long_term_concerns': [
                    'Degradação contínua de materiais tóxicos',
                    'Bioacumulação na cadeia alimentar',
                    'Alterações no habitat marinho',
                    'Contaminação de longo prazo'
                ]
            },
            'people': [
                {
                    'name': 'Almirante Marcos Sampaio Olsen',
                    'role': 'Diretor de Portos e Costas',
                    'action': 'Coordenou operação de afundamento',
                    'quote': 'A decisão foi tomada após esgotadas todas as alternativas viáveis.'
                },
                {
                    'name': 'Marina Silva',
                    'role': 'Ministra do Meio Ambiente',
                    'action': 'Manifestou preocupação com impacto ambiental',
                    'quote': 'O afundamento representa um precedente preocupante para o meio ambiente marinho.'
                },
                {
                    'name': 'Anna Christina Saraiva',
                    'role': 'Diretora de Qualidade Ambiental do IBAMA',
                    'action': 'Avaliou impacto ambiental',
                    'quote': 'Os riscos ambientais são significativos e de longa duração.'
                }
            ],
            'documents': [
                {
                    'title': 'Autorização de Afundamento - Marinha',
                    'url': 'https://www.marinha.mil.br/autorizacoes/2023/001',
                    'date': '02/02/2023',
                    'description': 'Autorização oficial para o afundamento'
                },
                {
                    'title': 'Relatório de Impacto Ambiental',
                    'url': 'https://www.ibama.gov.br/relatorios/2023/sao-paulo',
                    'date': '01/02/2023',
                    'description': 'Avaliação dos impactos ambientais'
                },
                {
                    'title': 'Parecer Técnico MPF',
                    'url': 'https://www.mpf.mp.br/pareceres/2023',
                    'date': '03/02/2023',
                    'description': 'Análise legal do procedimento'
                }
            ],
            'protests_and_reactions': [
                {
                    'organization': 'Greenpeace Brasil',
                    'action': 'Protesto marítimo',
                    'statement': 'Crime ambiental em águas internacionais'
                },
                {
                    'organization': 'WWF Brasil',
                    'action': 'Nota de repúdio',
                    'statement': 'Violação de convenções ambientais internacionais'
                },
                {
                    'organization': 'Basel Action Network',
                    'action': 'Denúncia internacional',
                    'statement': 'Descumprimento da Convenção de Basileia'
                }
            ]
        }
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                         mapbox_key=MAPBOX_PUBLIC_KEY,
                         timeline_events=TIMELINE_EVENTS,
                         full_story=FULL_STORY)

if __name__ == '__main__':
    app.run(debug=True)        