from flask import Flask, render_template, Blueprint

app = Flask(__name__)

appmain = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path='/main/static')

@appmain.route('/')
def index():
    image_urls = [
        "https://media.istockphoto.com/id/514472018/es/foto/hermosa-boda-par-abrazar-cerca-de-columnas.jpg?s=612x612&w=0&k=20&c=uNaI5B3WpsnZVff6l6jvyhZMXd-DIkQl7ZCjO2W92K0=",
        "https://media.istockphoto.com/id/498477061/es/foto/siente-el-d%C3%ADa-de-su-boda-bliss.jpg?s=612x612&w=0&k=20&c=kYex3_JmNNEz6CdYfclcwKjxj2GGln-NU9QyXKdlb5Y=",
        "https://media.istockphoto.com/id/530188882/es/foto/retrato-de-una-joven-pareja-de-novios.jpg?s=612x612&w=0&k=20&c=SeUr9mYN6ZJ1phUPg05577uSMtO8-u4bSgcda-DfAus="
    ]
    info_list = [
        {
            'image_url': 'https://media.istockphoto.com/id/1303804576/es/foto/nuestro-primer-baile.jpg?s=612x612&w=0&k=20&c=imONv7gNEBiPlOw-s_odejgfIaZ9QEI7eoBqmT0gVmM=',
            'text1': 'El amor es el idioma que todos entendemos.',
            'text2': 'El amor, esa fuerza mágica que impulsa a la humanidad, es un viaje intrincado de emociones, experiencias y compromisos. Va más allá de las palabras, manifestándose en pequeños gestos cotidianos y en los momentos extraordinarios que compartimos.'
        },
    ]
    return render_template('main.html', image_urls=image_urls, info_list=info_list)

