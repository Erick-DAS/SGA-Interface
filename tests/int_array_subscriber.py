import paho.mqtt.client as mqtt

user = "Casa31"
passwd = "c123EC4567"

Broker = "192.168.1.19"
Port = 1883
KeepAlive = 60

namespace = "snake_game"

#comeu_maca_topic = namespace + "/comeu_maca"
snake_pos_topic = namespace + "/snake_pos"

def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo " + str(rc))
    client.subscribe(snake_pos_topic, qos=0) 

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):
    # print(str(msg.topic)+" "+str(msg.payload.decode("utf-8")))

    #if (str(msg.topic) == comeu_maca_topic):
    #    if(str(msg.payload.decode("utf-8")) == "Estou apitando"):
    #        comeu_maca = True
    #    else:
    #        comeu_maca = False
#
    #    print(f'Comeu_maca = {comeu_maca}')

    if (str(msg.topic) == snake_pos_topic):
        print(str(msg.payload.decode("utf-8")))

    else:
        print("Erro! Mensagem recebida de tópico estranho")

    print("Recebi algo")

client = mqtt.Client()              
client.on_connect = on_connect      
client.on_message = on_message  

client.username_pw_set(user, passwd)


print("=================================================")
print("Teste Cliente MQTT")
print("=================================================")


client.connect(Broker, Port, KeepAlive)
client.loop_forever() 