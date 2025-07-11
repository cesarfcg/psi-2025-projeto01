from django.shortcuts import render

# Create your views here.
jogadores =  [
        {   
        "id": 1,
        "nome": "Agustín Rossi",
        "nome_completo": "Agustín Daniel Rossi",
        "idade": 29,
        "posicao": "Goleiro",
        "data_nascimento": "21/08/1995",
        "local_nascimento": "Buenos Aires, Argentina",
        "nacionalidade": "Argentino",
        "imagem": "website/img/rossi.jpg"
    },
    {
        "id": 2,
        "nome": "Guillermo Varela",
        "nome_completo": "Guillermo Varela Olivera",
        "idade": 31,
        "posicao": "Lateral-direito",
        "data_nascimento": "24/03/1993",
        "local_nascimento": "Montevidéu, Uruguai",
        "nacionalidade": "Uruguaio",
        "imagem": "website/img/varela.jpg"
    },
    {
        "id": 3,
        "nome": "Léo Pereira",
        "nome_completo": "Leonardo César Pereira",
        "idade": 28,
        "posicao": "Zagueiro",
        "data_nascimento": "31/01/1996",
        "local_nascimento": "Curitiba, Paraná, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/leopereira.jpg"
    },
    {
        "id": 4,
        "nome": "Léo Ortiz",
        "nome_completo": "Leonardo Rech Ortiz",
        "idade": 29,
        "posicao": "Zagueiro",
        "data_nascimento": "03/01/1996",
        "local_nascimento": "Porto Alegre, Rio Grande do Sul, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/leoortiz.jpg"
    },
    {
        "id": 5,
        "nome": "Alex Sandro",
        "nome_completo": "Alex Sandro Lobo da Silva",
        "idade": 34,
        "posicao": "Lateral-esquerdo",
        "data_nascimento": "26/01/1991",
        "local_nascimento": "Catanduva, São Paulo, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/alexsandro.jpg"
    },
    {
        "id": 6,
        "nome": "Jorginho",
        "nome_completo": "Jorge Luiz Frello Filho",
        "idade": 33,
        "posicao": "Volante",
        "data_nascimento": "20/12/1991",
        "local_nascimento": "Imbituba, Santa Catarina, Brasil",
        "nacionalidade": "Brasileiro e italiano",
        "imagem": "website/img/jorginho.jpg"
    },
    {
        "id": 7,
        "nome": "Jorge Carrascal",
        "nome_completo": "Jorge Andrés Carrascal Guardo",
        "idade": 26,
        "posicao": "Meia",
        "data_nascimento": "25/05/1998",
        "local_nascimento": "Cartagena, Colômbia",
        "nacionalidade": "Colombiano",
        "imagem": "website/img/rossi.jpg"
    },
    {
        "id": 8,
        "nome": "Erick Pulgar",
        "nome_completo": "Erick Antonio Pulgar Farfán",
        "idade": 30,
        "posicao": "Volante",
        "data_nascimento": "15/01/1994",
        "local_nascimento": "Antofagasta, Chile",
        "nacionalidade": "Chileno",
        "imagem": "website/img/pulgar.jpg"
    },
    {
        "id": 9,
        "nome": "Giorgian De Arrascaeta",
        "nome_completo": "Giorgian Daniel De Arrascaeta Benedetti",
        "idade": 30,
        "posicao": "Meia-ofensivo",
        "data_nascimento": "01/06/1994",
        "local_nascimento": "Nuevo Berlín, Uruguai",
        "nacionalidade": "Uruguaio",
        "imagem": "website/img/gostoso.jpg"
    },
    {
        "id": 10,
        "nome": "Pedro",
        "nome_completo": "Pedro Guilherme Abreu dos Santos",
        "idade": 27,
        "posicao": "Centroavante",
        "data_nascimento": "20/06/1997",
        "local_nascimento": "Rio de Janeiro, RJ, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/pedro.jpg"
    },
    {
        "id": 11,
        "nome": "Bruno Henrique",
        "nome_completo": "Bruno Henrique Pinto",
        "idade": 34,
        "posicao": "Atacante",
        "data_nascimento": "30/12/1990",
        "local_nascimento": "Belo Horizonte, Minas Gerais, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/bh.jpg"
    },
    {
        "id": 12,
        "nome": "Filipe Luís",
        "nome_completo": "Filipe Luís Kasmirski",
        "idade": 39,
        "posicao": "Treinador",
        "data_nascimento": "09/08/1985",
        "local_nascimento": "Jaraguá do Sul, Santa Catarina, Brasil",
        "nacionalidade": "Brasileiro",
        "imagem": "website/img/filipe.png"
    }
]
ultimos_jogos = [
    {
        "data": "29/06/2025",
        "campeonato": "Super Mundial de Clubes",
        "estadio": "Hard Rock Stadium",
        "time_casa": "Flamengo",
        "placar_casa": 2,
        "placar_visitante": 4,
        "time_visitante": "FC Bayern München"
    },
    {
        "data": "24/06/2025",
        "campeonato": "Super Mundial de Clubes",
        "estadio": "Camping World Stadium",
        "time_casa": "Flamengo",
        "placar_casa": 1,
        "placar_visitante": 1,
        "time_visitante": "Los Angeles FC"
    }
]

proximo_jogo = {
    "data": "12/07/2025",
    "campeonato": "Brasileirão",
    "estadio": "Maracanã",
    "time_casa": "Flamengo",
    "time_visitante": "São Paulo"
}
noticias = [
    {   
        "id":1,
        "titulo": "Flamengo anuncia novo reforço para 2025",
        "data": "05/07/2025",
        "resumo": "O clube confirmou a contratação do meia que promete reforçar o elenco para a próxima temporada.",
        "imagem":"website/img/jorginhoanuncio.jpg",

    },
    {
        "id":2,
        "titulo": "Flamengo inicia semana de treinos visando o retorno do Brasileirão",
        "data": "08/07/2025",
        "resumo": "Mais Querido enfrenta o São Paulo no próximo sábado (12), às 16h30, no Maracanã",
        "imagem":"website/img/reestreia.jpg",
    },
]
introducao = {"introducao":"O Clube de Regatas do Flamengo, carinhosamente conhecido como Mengão, é uma das maiores instituições esportivas do Brasil e do mundo. Fundado em 17 de novembro de 1895, no Rio de Janeiro, o clube nasceu como uma agremiação de remo e, ao longo do tempo, se transformou em um gigante do futebol. Com uma história repleta de títulos e ídolos inesquecíveis, o Flamengo acumula conquistas nacionais e internacionais, como a Copa Libertadores da América e o Campeonato Brasileiro. A Nação Rubro-Negra, como é conhecida sua apaixonada torcida, é a maior do país e uma das mais fervorosas do planeta. Mais do que um clube, o Flamengo é um símbolo de paixão, raça e glória."}

context = {"jogadores":jogadores,"ultimos_jogos":ultimos_jogos,"proximo_jogo":proximo_jogo , "introducao":introducao,"noticias":noticias}

def index(request):
    return render(request,'website/index.html',context )
def elenco(request):
    context = {"jogadores":jogadores}
    return render(request,'website/elenco.html',context,)
def sobre(request):
    return render(request,'website/sobre.html')
def jogador(request,id_jogador):
    return render(request,"website/jogador.html",jogadores[id_jogador - 1])
def noticia(request,id_noticia):
    return render(request,"website/noticia.html",noticias[id_noticia - 1])