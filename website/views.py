from django.shortcuts import render,get_object_or_404
from . models import Jogador,Jogo,Noticia,Introducao,ProximoJogo,Credito,Autor,Sobre
from datetime import date
# Create your views here.

# ultimos_jogos = [
#     {
#         "data": "29/06/2025",
#         "campeonato": "Super Mundial de Clubes",
#         "estadio": "Hard Rock Stadium",
#         "time_casa": "Flamengo",
#         "placar_casa": 2,
#         "placar_visitante": 4,
#         "time_visitante": "FC Bayern München"
#     },
#     {
#         "data": "24/06/2025",
#         "campeonato": "Super Mundial de Clubes",
#         "estadio": "Camping World Stadium",
#         "time_casa": "Flamengo",
#         "placar_casa": 1,
#         "placar_visitante": 1,
#         "time_visitante": "Los Angeles FC"
#     }
# ]

# proximo_jogo = {
#     "data": "12/07/2025",
#     "campeonato": "Brasileirão",
#     "estadio": "Maracanã",
#     "time_casa": "Flamengo",
#     "time_visitante": "São Paulo"
# }
# noticias = [
#     {   
#         "id":1,
#         "titulo": "Flamengo anuncia novo reforço para 2025",
#         "data": "05/07/2025",
#         "resumo": "O clube confirmou a contratação do meia que promete reforçar o elenco para a próxima temporada.",
#         "imagem":"website/img/jorginhoanuncio.jpg",

#     },
#     {
#         "id":2,
#         "titulo": "Flamengo inicia semana de treinos visando o retorno do Brasileirão",
#         "data": "08/07/2025",
#         "resumo": "Mais Querido enfrenta o São Paulo no próximo sábado (12), às 16h30, no Maracanã",
#         "imagem":"website/img/reestreia.jpg",
#     },
# ]
# introducao = {"introducao":"O Clube de Regatas do Flamengo, carinhosamente conhecido como Mengão, é uma das maiores instituições esportivas do Brasil e do mundo. Fundado em 17 de novembro de 1895, no Rio de Janeiro, o clube nasceu como uma agremiação de remo e, ao longo do tempo, se transformou em um gigante do futebol. Com uma história repleta de títulos e ídolos inesquecíveis, o Flamengo acumula conquistas nacionais e internacionais, como a Copa Libertadores da América e o Campeonato Brasileiro. A Nação Rubro-Negra, como é conhecida sua apaixonada torcida, é a maior do país e uma das mais fervorosas do planeta. Mais do que um clube, o Flamengo é um símbolo de paixão, raça e glória."}
# sobre = {
#     "info": "Este site foi desenvolvido com o objetivo de demonstrar conhecimentos em desenvolvimento web utilizando o framework Django. Ele apresenta informações organizadas, com funcionalidades como:"
#     }
# autores = [
#     {
#         "nome":"Fernando César Campos Gonzaga",
#         "email":"fernandocesar4141@gmail.com",
#     },
# ]
# creditos = {"creditos":"As informações e imagens utilizadas no site são de fontes públicas e têm finalidade exclusivamente educacional."}

# context = {"ultimos_jogos":ultimos_jogos,"proximo_jogo":proximo_jogo , "introducao":introducao,"noticias":noticias, "sobre":sobre, "autores":autores,"creditos":creditos}

def index(request):
    noticias = Noticia.objects.all()
    introducao = Introducao.objects.first()
    jogos = Jogo.objects.all()
    proximojogo = ProximoJogo.objects.all()
    context = {"noticias":noticias, "introducao":introducao,"jogos":jogos,"proximojogo":proximojogo}
    return render(request,'website/index.html',context )
def elenco(request,):
    jogadores = Jogador.objects.all()
    return render(request,'website/elenco.html',{"jogadores":jogadores})
def sobre(request):
    sobre = Sobre.objects.all()
    creditos = Credito.objects.first()
    autores = Autor.objects.all()
    context = {"creditos":creditos,"autores":autores,"sobre":sobre}
    return render(request,'website/sobre.html',context)
def jogador(request,id_jogador):
    jogadores = get_object_or_404(Jogador,id = id_jogador)
    return render(request,"website/jogador.html",{"jogadores":jogadores})
def noticia(request,id_noticia):
    noticias = get_object_or_404(Noticia,id = id_noticia)
    return render(request,"website/noticia.html",{"noticias":noticias})