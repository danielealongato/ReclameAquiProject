def save_csv_by_df(informacoes):
    df = {}
    for item in informacoes:
    # Criar um DataFrame com os dados coletados
        df = pd.DataFrame({
            'id': item.get("id"),
            'Titulo': item.get("title"),
            'Status': item.get("status"),
            'description': item.get("description"),
            'created': item.get("created"),
            'solved': item.get("solved")
        })

    # Salvar os dados em um arquivo CSV
    #df.to_csv('reclamacoes_inss.csv', index=False, encoding='utf-8-sig')

    ---------------

    # Exemplo de payload
    payload = [{
        "prev": [],
        "next": [],
        "data": [
            {
                "created": "2024-06-23T09:58:37",
                "description": "Uma associação que não conheço está descontando mensalidade, que NÃO autorizei",
                "solved": False,
                "evaluated": False,
                "id": "8I0-BHsbcXgLXaAP",
                "title": "Desconto não autorizado",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T17:54:46",
                "description": "Fiz uma perícia dia 03 de júnior liguei e a atendente disse que meu benefício foi concedido mas não parece valor nem local de pagamento fui atropelada dia 28 de julho e já faz praticamente um ano que estou aguardando meu direitos a serem compridos e exercidos e vcs ajudam em nada só peço até pelo amor de Deus librem meu valor todo correto pois deu entrada em outubro tanto pela distancia como marquei presencialmente e foi remarcado várias vezes estou no quadro ansioso depressivo sem sair de casa sem andar dependendo dos outros parentes amigos que né ajudam no que podem tenho todo mês retorno com médico na cidade mas nem em todos posso ir devido não poder pagar o carro pra mim levar remédio exames isso nem posso também fico sentindo dor igual animal brabo alimentação adequada não posso tenho duas filhas animal que dependem de mim e não posso trabalhar nem me virar atrás de nada ai me diz se isso é certo inss dificultar a vida de quem precisa quero meu valor corretamente total o que tenho por diretos e liberem logo pois já sofri muito e sofro vcs são tão ruim que já até mandei diversos e-mail e nenhum com resposta claras e objetivas",
                "solved": False,
                "evaluated": False,
                "id": "zXh-eagStpfqAbX1",
                "title": "Liberação total do benefício",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T17:31:53",
                "description": "Sou uma gestante de alto risco tenho hidrocefalia e estou tendo quadros de infecção de urinária indo pra 3 vez e sinto muito dor nas costas devido isso estou tendo pegar muito atestado por conta dor na lombar e pegar peso pois eu trabalho em loja de roupa na Pernambucanas que tem várias escadas e não tenho acento adequado trabalho 8 horas de pe por conta dor nas costas tenho queda de pressão a última foi 8x3 ontem fui pegar carta de afastamento da empresa tenho perícia dia 25/06 preciso ser afastada até final gestação irei pegar carta na médica dia 2 de julho q próxima consulta no sinhá Junqueira em Ribeirão preto natal alto risco estou 22 semanas precisava afastar até final gestação por conta dores na lombar e minha queda de pressão que se torna risco pois última vez quase caio da escada por conta disso",
                "solved": False,
                "evaluated": False,
                "id": "eabk4tZUiV0dcYR8",
                "title": "Preciso ser afastada por causa da gravidez de alto risco",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T16:12:51",
                "description": "Vendo o valor que receberei em junho de 2024, reparei que estava abaixo do normal. Verifiquei que que em abril , maio e junho de 2024 fui descontada indevidamente de R$ 39,53 destinado a contribuição Conafer 0800 940 1285. Nunca pedi tal contribuição, nem sei para que serve. Peço o cancelamento desta cobrança e o ressarcimento dos valores cobrados indevidamente corrigidos o mais rápido possível",
                "solved": False,
                "evaluated": False,
                "id": "IByYd6VPb4Eiv-9F",
                "title": "Cobrança [Editado pelo Reclame Aqui] Conafer",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T15:50:04",
                "description": "Quero relatar oque sofri nas 2 últimas perícias feitas, sofri se fibromialgia e hérnias de disco na coluna cervical, torácica e lombar,doenças crônicas. <br /><br />Prezados, após eu ter realizado inúmeras reclamações e denúncias referente a minha perícia realizada em 17 de MAIO de 2024 NB:*******<br />N do requerimento: 216531330.<br />Foi autorizado uma nova perícia médica, agendei com a data mais próxima  que tinha disponível no sistema,  07 de JUNHO de 2024, escolhi outro posto do inss, endereço da Praça da Bandeira, com receio de ser atendida pelo perito que sofri maus tratos na agência do endereço de Ramos, local que é mais próximo da minha residência no bairro de Olaria. A  nova perita me perguntou se tinha levado novos documentos (laudos e exames) eu respondi que não, e o que  tenho estavam todos recentemente feitos. Pediu para dar uma olhada e devolveu sem ler e disse isso tudo ja tem no sistema,  você fez uma perícia agora e ja sei de tudo!  Acrescentei que o sisreg só conseguiu data disponível para uma nova consulta em 25/06/2024 com o ortopedista que já faço tratamento Dr. Luiz Felipe Gouveia da Silva ( CRM*******) o mesmo que realizou o laudo em 16/04/2024 com pedido de aposentadoria. <br />A consulta com a reumatologista que trata da minha doença de fibromialgia  Dra. Johana de Lurdes Castilho (CRM 521263455) fez o laudo rescente 11/04/2024, ela agendou retorno para 11/07/2024. Data que terei que receber novas receitas para compra das medicações que faço uso da doença já diagnostica pela mesma (fibromialgia).<br />Falei ainda que o Sisreg não tem vaga para consulta solicitada pelo médico para clínica da dor, liguei em 05/06/2024 para ouvidoria da saúde solicitando uma urgência no pedido feito pela clinica da familia SMS CF Klebel  De Oliveira Rocha pela medica Livia Maria da Silva ao Sisreg em 26/04/2024, pois estou sofrendo com muitas dores referente a cervical e a fibromialgia ( protocolo da solicitação: rio28938508-0 atendente Elaine) e também não foi agendada a consulta solicitada pelo médico para clínica da família ao Neurocirurgião no sistema do SER: 5473306, também solicitei no dia 05/06/2024 a ouvidoria da saúde (protocolo da solicitação rio28938384-2 atendente Elaine) levei tudo para mostrar a perita minha angústia aguardando o que preciso para amenizar meu sofrimento com as dores, quis provar com os protocolos e o sistema do sisreg me indicando na fila para atendimento, não deu importância no meu assunto, se levantou indo para porta e fechando com a chave(disse está vendo que tranquei né) respondi que sim, sem entender o porque,  ela mandou eu tirar toda minha roupa e ficar nua, disse que era necessário essa analise completa do meu corpo (nunca tinha passado por isso, me senti constrangida), tenho vergonha das queimaduras que tenho no corpo de asfalto do acidente, inclusive tenho liberação no sisreg para o hospital do Andarai de queimados para retira las, só não tive coragem, estive na consulta e fui informada que teria que raspar a carne que está morta nas nádegas, não tenho coragem ainda, enfim tirei a roupa toda e ela  mandou eu rodar meu corpo, sentar na cama e se levantar, em seguida,  falou agora coloca a roupa e está liberada,  só olhar a resposta no site as 21h.<br />Fiz como mandou, entrei nesse horário e não tinha resposta,  liguei para a central 135 e foi me passado o resultado de Indeferimento do meu pedido. <br />Enfim,  mais uma vez sofri com constrangimento na perícia médica do inss,  tenho certeza que ela fez isso tudo poque leu o meu relato no sistema do inss reclamando do perito anterior. Ela me fez passar por essa situação constrangedora, tenho vergonha de ficar sem roupa na frente de qualquer pessoa,  pois tenho marcas do acidente que me causam angústia e muita  vergonha, ela colocar no laudo as tatuagens foi o mesmo de dizer que meu corpo tem marchas,  pq é a verdade, tenho prontuário dizendo que me queimei, tem autorização no sistema para hospital de queimaduras, faço tratamento psicológico pq sofro com meu rosto marcado e meu corpo, passar por isso e ela ainda me negar o pedido para proteger o colega de profissão. <br />Ressalto que em momento nenhum realizou algum tipo de exame físico, copiou e colou oque já tinha do perito anterior, nao entendi para que pediram para eu repetir a pericia, se ela nao me examinou??? só acrescentou peso, altura que me perguntou, colocou  as tatuagens como se fosse pecado ou proibido para doentes, parece que cometi um [Editado pelo Reclame Aqui]! Achei preconceituoso a forma que descreveu! Isso nao foi nada profissional a forma que me expôs, nao fui la para isso!? Fiz sim,  tentado esconder as queimaduras e mesmo assim nao deu certo,  só olhou meu corpo a distância e fez um relato de marcas de sol e tatuagem,  eu tenho tatuagem sim, fiz em cima das cicatrizes do asfalto quando sofri o acidente para apagar as manchas de queimadura horríveis que ficou no meu corpo, e marca de biquíni não tenho, sou morena , não sou branca,  tive que tirar fotos do meu corpo para registrar a [Editado pelo Reclame Aqui] denúncia da perita. Ela não considerou meu laudo da reumatologista da doença caracterizada como crônica de fibromialgia cid 10: M79.7, não considerou o laudo do traumatologista e ortopedista informando os cid: M542 / M545 / M797 / M500 / M519 da doença diagnosticada por ele,  ela não considerou meus exames e ressonâncias magnéticas relatando as hérnias de disco na cervical e comprimindo minha medula, torácica e lombar que já virou artrose,  ela não considerou o laudo de exame de eletroneuromiografia feitos da parte superior e inferior informando que estou com dedo unelar com nervo afetado,  relatei minha espera do Neurocirurgião e clínica da dor com protocolo de reclamação no sistema de saúde SER: 5473306. Ela só considerou minha tatuagem  e minha cor morena, sou descendente de negro, não sou branca, estou com corpo manchado da queimaduras! Ela não se preocupou com os remédios caros que preciso tomar e nao tenho outra fonte de renda para comprar! Nao tenho condições fisicas e psicológicas para trabalhar! Sempre trabalhei,  tengo carteira assinada desde os meu 18 anos, da forma que estão fazendo é como se eu fosse preguiçosa querendo dinheiro do governo atoa, isso me da vergonha! Estou passando por peritos que ignoram laudos e exames do proprio SUS. Quero saber como irei comprar minha medição das duas doenças que o SUS não distribuí,  a rede pública não possui,  são caros e não dura 30 dias, os medicos me dão receitas para 60 ou 90 dias, estou desempregada sem poder voltar a trabalhar pelas dores fortes,  estou aguardando o SUS liberar o Neurocirurgião e a Clinica da dor. A medição me faz ter ocusto de R$ 600,00 por mês. Estou sem pagar minhas despesas de casa para sobrar para os remédios,  tenho dois filhos menores de idade, a renda do meu companheiro não dá para pagar tudo! Já entrei com processo na justiça pedindo ajuda! Agora estou aqui novamente fazendo queixa do que venho passando com o sistema do inss, preciso que alguém me ouça e me ajude, que algum órgão do governo ou do estado tome atitude e possa entervir na minha situação de sofrimento, angústia, constrangimento, vergonha,preconceito, acedio e dor consiga me ajudar. <br /><br />Obs: Estou fazendo tratamento emocional conforme orientação dos médicos, e os peritos do inss estão acabando comigo, não tenho mais forças para lutar contra esse sistema desumano do estado do Rj. Estou muito cansada, não aguento mais sofrer todo dia com tanta dor tenho FIBROMIALGIA existe lei e decreto para essa doença que é ignorada pelo sistema do sus e do inss, sinto dor no corpo todo ! os peritos ignoram esse problema, parecendo laudo sem efeito legal, não aguento mais nao ter dinheiro para comprar os remédios e ter que pedir aos familiares dinheiro para ajudar! se eu tentar suicídio e morrer quero que o estado indenize minha família para custear os gastos com meus dois filhos menores. Infelizmente estou aguardando liberação do estado com médico Neurocirurgião. Quero muito viver e terminar de criar meus filhos, mais sofrendo com essas dores sem recurso nenhum e ainda sendo prejudicada como se estivesse inventando tudo, é desanimador. Me perdoem mais nao teve jeito, estou mandando foto do corpo queimado de sol e marca de biquíni relatado pela perita médica ( deve ter feito confusão de paciente)! Outra coisa, gostaria de saber se doente não pode ter tatuagem no corpo? a tatuagem tem data de quando foi feita no meu corpo? Isso foi preconceito e falta de respeito com quem está precisando de ajuda financeira e médica. Não solicitei uma nova perícia médica para passar por constrangimento, não fui lá só para ficar nua, ser avaliada como se fosse vaga para trabalho de modelo! Um médico quando manda um paciente ficar despido ele entrega um roupão para não ficar contrangido,  ela me fez ficar completamente nua, rodar para olhar meu corpo todo e me dizer que poderia olhar o aplicativo.  Isso é um absurdo! Minha fibromialgia está na crise por conta de tudo isso que venho passando.... espero que meu desabafo seja escutado, estou desanimada com tanta injustiça, até quem jurou cuidar da saúde das pessoas está matando de sofrimento. <br /><br />Filha: Ana clara.<br />Data de nascimento: 03/03/2014<br /><br />Filho: Luis Guilherme.<br />Data de nascimento: 02/08/2022<br /><br /><br /><br /><br />1 - NB:*******<br />N do requerimento: 216531330<br /><br />2 - NB:*******<br />N do requerimento: 422965622<br /><br />*******.<br />E-mail: *******",
                "solved": False,
                "evaluated": False,
                "id": "oucOqxv0aSpphXvC",
                "title": "Falta de ética,respeito, abuso,constrangimento, profissionalismo danos morais de peritos do INSS da Agencia de Ramos e Agencia da Praça da Bandeira",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T14:53:56",
                "description": "&quot;Ocorreu um erro ao buscar seus dados.&quot;<br />Estou recebendo essa mensagem ja tem uma semana e não consigo fazer nada dentro da plataforma do inss.",
                "solved": False,
                "evaluated": False,
                "id": "SPZ_DJkrA2XCwhMq",
                "title": "BLOQUEIO DE ACESSO",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T09:49:47",
                "description": "Desde o dia 26/03/2024, não tenho resposta da revisão do pagamento, pois colocarão a data incorreta. Ligo no 135 e fala que tem que esperar já estou esperando a 3 meses e não recebi nem uma posição..",
                "solved": False,
                "evaluated": False,
                "id": "C90tlLR6rv-pVnX1",
                "title": "Revisão administrativa",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-22T09:44:36",
                "description": "Estou doente entrei com ação contra o INSS pra ver se recebo um auxílio em consequência do meu problema de saude",
                "solved": False,
                "evaluated": False,
                "id": "Rsj6so8iLRftrpxF",
                "title": "Já fiz todas as perícias marca doença infecção venosa na perna esquerda burrice tendente e até agora não tenho resultado",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-21T20:16:26",
                "description": "Desde quando tirei a carteira de trabalho com 16 anos, não consigo resolver esse problema, hoje tenho 26 anos e estou impossibilitada de assinar minha carteira, pedir auxilio doença, entre outras coisas, pois não consigo simplesmente agendar horário e ir na agencia atualizar meus dados, sendo que quando vou presencialmente não me atendem e quando ligo tentando marcar horário, por estar com nome de outra pessoa constando no meu cpf não consigo atendimento, já fui na receita federal estar tudo ok, já fui na caixa tudo ok, o problema realmente é que costa uma pessoa do piau, sendo que sou de salvador, pelo amor de Deus  me ajudem.",
                "solved": False,
                "evaluated": False,
                "id": "lOvCq29ux4UfS5fq",
                "title": "Atualizaram os dados de outra pessoa e colocaram como se fossem meus.",
                "userName": "****",
                "status": "PENDING"
            },
            {
                "created": "2024-06-21T17:10:08",
                "description": "Já estou no 3 mês que estão descontando 39 reais em cima do meu dinheiro que recebo todos os meses, sou pensionista. EU NUNCA AUTORIZEI desconto algum e não tenho nem ideia de onde isso procede. Eu não sei mais o que fazer.",
                "solved": False,
                "evaluated": False,
                "id": "gnFn-ilbH1fDzEkp",
                "title": "Desconto indevido",
                "userName": "****",
                "status": "PENDING"
            }
        ],
        "count": [],
        "maxScore": [],
        "aggregations": [],
        "extraData": []
    }]