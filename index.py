import telepot
from telepot.loop import MessageLoop
import requests

bot = telepot.Bot("696587140:AAHTOkVKMI-Tw1FE97iZFqVgZmkRkuhoi0Q")

def main(msg):
 if("text" in msg):
  text = msg["text"]
 else:
  text = ""
 id1 = msg["chat"]["first_name"]
 id2 = msg["chat"]["id"]
 id3 = msg["chat"]["username"]
 id4 = msg["from"]["language_code"]

 if(text.upper() == "/START"):
  bot.sendMessage(id2, f"""OLÁ <b>{id1}!</b> Seja Bem Vindo Ao <b>THICAZYROBOT</b> Digite o Comando /ferramentas para visualizar meu menu""", "html")
 if(text.upper() == "/FERRAMENTAS"):
  bot.sendMessage(msg["chat"]["id"], """<b> MINHAS FERAMENTAS!!!</b>

<b>[+] CONSULTAS [+]</b>
 <b>Consulta CPF</b> - /cpf
 <b>Consulta CNPJ</b> - /cnpj
 
<b>[+] EXTRA [+]</b>
 <b>USER Info</b> - /id

<b> [+]CONTATO </b>
 <b>Dono BOT:</b> @ThiCrazy
 <b>Grupo BOT:</b> @ThiCrazyCPF

<b>BY:</b> @ThiCrazyRoBOT""", parse_mode="html", reply_to_message_id=msg["message_id"])

 if(text.upper() == "/CPF"):
  bot.sendMessage(id2, """<b>Está Faltando Algo Não Acha?</b>
   
<b>EXEMPLO:</b>
 <pre>/cpf 76662195804</pre>""", "html", reply_to_message_id=msg["message_id"])

 if(text.split()[0].upper() == "/CPF" and text.split()[1]):
  try:
   cpf = text.split()[1]
   url = "https://thicrazyconsultascpf.000webhostapp.com/api.php?cpf="+cpf
   api = requests.get(url)
   if(api.text == ""):
    bot.sendMessage(chat, "<b>CPF NAO ENCONTRADO!</b>", "html")
   else:
    api = api.json()
    #cpf
    if("cpf" in api):
     cpf = api["cpf"]
     if(cpf == ""):
      cpf = "Não encontrado!"
    #nome
    if("nome" in api):
     nome = api["nome"]
     if(nome == ""):
      nome = "Não encontrado!"
    #nomeMae 
    if("mae" in api):
     mae = api["mae"]
     if(mae == ""):
      mae = "Não encontrado!"
    #sexo
    if("sexo" in api):
     sexo = api["sexo"]
     if(sexo == ""):
      sexo = "Não encontrado!"
    #nascimento
    if("nascimento" in api):
     nascimento = api["nascimento"]
     if(nascimento == ""):
      nascimento = "Não encontrado!"
    #idade
    if("idade" in api):
     idade = api["idade"]
     if(idade == ""):
      idade = "Não encontrado!"
    #endereço
    if("endereco" in api):
     endereco = api["endereco"]
     if(endereco == ""):
      endereco = "Não encontrado!"
    #bairro
    if("bairro" in api):
     bairro = api["bairro"]
     if(bairro == ""):
      bairro = "Não encontrado!"
    #cidade
    if("cidade" in api):
     cidade = api["cidade"]
     if(cidade == ""):
      cidade = "Não encontrado!"
    #cep
    if("cep" in api):
     cep = api["cep"]
     if(cep == ""):
      cep = "Não encontrado!"
    bot.sendMessage(id2, f"""<b>DADOS ENCONTRADOS!</b>
    
<b>CPF:</b> <pre>{cpf}</pre>
<b>NOME:</b> <pre>{nome}</pre>
<b>MAE:</b> <pre>{mae}</pre>
<b>SEXO:</b> <pre>{sexo}</pre>
<b>NASCIMENTO:</b> <pre>{nascimento}</pre>
<b>IDADE:</b> <pre>{idade}</pre>
<b>ENDEREÇO:</b> <pre>{endereco}</pre>
<b>BAIRRO:</b> <pre>{bairro}</pre>
<b>CIDADE:</b> <pre>{cidade}</pre>
<b>CEP:</b> <pre>{cep}</pre>
<b>BY:</b> @ThiCrazyRoBOT""", "html", reply_to_message_id=msg["message_id"])
  except:
   bot.sendMessage(id2, "<b>CPF NAO ENCONTRADO!</b>", "html", reply_to_message_id=msg["message_id"])

 if(text.upper() == "/CNPJ"):
  bot.sendMessage(id2, """<b>Está Faltando Algo Não Acha?</b>
   
<b>EXEMPLO:</b>
 <pre>/cnpj 03264986000103</pre>""", "html", reply_to_message_id=msg["message_id"])
 if(text.split()[0].upper() == "/CNPJ" and text.split()[1]):
  try:
   cnpj = text.split()[1]
   url = "https://www.receitaws.com.br/v1/cnpj/"+cnpj
   api = requests.get(url)
   if(api.text == ""):
    bot.sendMessage(chat, "<b>CNPJ NÃO ENCONTRADO!</b>", "html")
   else:
				api = api.json()		
				#Atividade_Principal
				if("text" in api["atividade_principal"][0]):
					atividade_principal = api["atividade_principal"][0]["text"]
					if(atividade_principal == ""):
						atividade_principal = "Não encontrado!"
					
				#Código
				if("code" in  api["atividade_principal"][0]):
					codigo = api["atividade_principal"][0]["code"]
					if(codigo == ""):
						codigo = "Não encontrado!"
						
				#Atividade_secundaria
				if("text" in api["atividades_secundarias"]):
					atividade2 = api["atividades_secundarias"][0]["text"]
				else:
					atividade2 = "Não encontrado!"
					
				#code2
				if("code" in api["atividades_secundarias"][0]):
					codigo2 = api["atividades_secundarias"][0]["code"]
				else:
					codigo2 = "Não encontrado!"
				
				#Data
				if("data_situacao" in api):
					data = api["data_situacao"]
				else:
					data = "Não encontrado!"
						
				#CNPJ
				if("cnpj" in api):
					cnpj = api["cnpj"]
				else:
					cnpj = "Não encontrado!"
						
				#Endereço	
				if("nome" in api):
					endereco = api["nome"]
				else:
					endereco = "Não encontrado!"
					
				#Efr
				if("efr" in api):
					efr = api["efr"]
				else:
					efr = "Não encontrado!"

				#Complemento
				if("complemento" in api):
					complemento = api["complemento"]
				else:
					complemento = "Não encontrado!"
		
				#UF
				if("uf" in api):
					uf = api["uf"]
				else:
					uf = "Não encontrado!"
	
				#Telefone
				if("telefone" in api):
					telefone = api["telefone"]
				else:
					telefone = "Não encontrado!"

				#Email
				if("email" in api):
					email = api["email"]
				else:
					email = "Não encontrado!"
		
				#Integrantes
				if("qsa" in api):
					qsa = api["qsa"][0]["nome"]
				else:
					qsa = "Não encontrado!"
				
				if("qsa" in api):
					qsa2 = api["qsa"][0]["qual"]
				else:
					qsa2 = "Não encontrado!"
					
				if("qsa" in api):
					qsa3 = api["qsa"][1]["nome"]
				else:
					qsa3 = "Não encontrado!"
				if("qsa" in api):
					qsa4 = api["qsa"][1]["qual"]
				else:
					qsa4 = "Não encontrado!"
		
				#Situação
				if("situacao" in api):
					situacao = api["situacao"]
				else:
					situacao = "Não encontrado!"
						
				#Bairro
				if("bairro" in api):
					bairro = api["bairro"]
				else:
					bairro = "Não encontrado!"
		
				#Rua
				if("logradouro" in api):
					rua = api["logradouro"]
				else:
					rua = "Não encontrado!"
		
				#Numero
				if("numero" in api):
					numero = api["numero"]
				else:
					numero = "Não encontrado!"
					
				#Cep
				if("cep" in api):
					cep = api["cep"]
				else:
					cep = "Não encontrado!"
						
				#Municipio
				if("municipio" in api):
					municipio = api["municipio"]
				else:
					municipio = "Não encontrado!"
		
				#Abertura
				if("abertura" in api):
					abertura = api["abertura"]
				else:
					abertura = "Não encontrado!"
	
				#Natureza_juridica
				if("natureza_juridica" in api):
					natureza_juridica = api["natureza_juridica"]
					if(natureza_juridica == ""):
						natureza_juridica = "Não encontrado!"
		
				#Fantasia
				if("fantasia" in api):
					fantasia = api["fantasia"]
					if(fantasia == ""):
						fantasia = "Não encontrado!"

				#Ultima_atualizacao
				if("ultima_atualizacao" in api):
					ultima_atualizacao = api["ultima_atualizacao"]
					if(ultima_atualizacao == ""):
						ultima_atualizacao = "Não encontrado!"
						
				#Status
				if("status" in api):
					status = api["status"]
					if(status == ""):
						status = "Não encontrado!"
						
				#Tipo
				if("tipo" in api):
					tipo = api["tipo"]
					if(tipo == ""):
						tipo = "Não encontrado!"
					
				#Motivo_Situacao
				if("motivo_situacao" in api):
					motivo_situacao = api["motivo_situacao"]
					if(motivo_situacao == ""):
						motivo_situacao = "Não encontrado!"

				#Situacao_especial
				if("situacao_especial" in api):
					situacao_especial = api["situacao_especial"]
					if(situacao_especial == ""):
						situacao_especial = "Não encontrado!"
					
				#Data_situacao_especial
				if("data_situacao_especial" in api):
					data_situacao_especial = api["data_situacao_especial"]
				if(data_situacao_especial == ""):
					data_situacao_especial = "Não encontrado!"

				#Capital Social
				if("capital_social" in api):
					capital_social = api["capital_social"]
					if(capital_social == ""):
						capital_social = "Não encontrado!"
					
				#Extra
				if("extra" in api):
					extra = api["extra"]
					if(extra == ""):
						extra = "Não encontrado!"
						
				bot.sendMessage(id2, f"""<b>DADOS DO ENCONTRADOS!!</b>

<b>CNPJ:</b> <pre>{cnpj}</pre>
<b>ATIVIDADE PRINCIPAL:</b> <pre>{atividade_principal}</pre>
<b>CÓDIGO:</b> <pre>{codigo}</pre>
<b>ATIVIDADE SECUNDÁRIA:</b> <pre>{atividade2}</pre>
<b>CÓDIGO:</b> <pre>{codigo2}</pre>
<b>DATA SITUAÇÃO:</b> <pre>{data}</pre>
<b>ENDEREÇO:</b> <pre>{endereco}</pre>
<b>EFR:</b> <pre>{efr}</pre>
<b>COMPLEMENTO:</b> <pre>{complemento}</pre>
<b>UF:</b> <pre>{uf}</pre>
<b>TELEFONE:</b> <pre>{telefone}</pre>
<b>EMAIL:</b> <pre>{email}</pre>
<b>SITUAÇÃO:</b> <pre>{situacao}</pre>
<b>BAIRRO:</b> <pre>{bairro}</pre>
<b>RUA:</b> <pre>{rua}</pre>
<b>NÚMERO:</b> <pre>{numero}</pre>
<b>CEP:</b> <pre>{cep}</pre>
<b>MUNICÍPIO:</b> <pre>{municipio}</pre>
<b>ABERTURA:</b> <pre>{abertura}</pre>
<b>NATUREZA JURÍDICA:</b> <pre>{natureza_juridica}</pre>
<b>FANTASIA:</b> <pre>{fantasia}</pre>
<b>ULTIMA ATUALIZAÇÃO:</b> <pre>{ultima_atualizacao}</pre>
<b>STATUS:</b> <pre>{status}</pre>
<b>TIPO:</b> <pre>{tipo}</pre>
<b>MOTIVO_SITUAÇÃO:</b> <pre>{motivo_situacao}</pre>
<b>SITUAÇÃO ESPECIAL:</b> <pre>{situacao_especial}</pre>
<b>DATA DA SITUAÇÃO Especial:</b> <pre>{data_situacao_especial}</pre>
<b>CAPITAL SOCIAL:</b> <pre>{capital_social}</pre>
<b>EXTRA:</b> <pre>{extra}</pre>

<b>INTEGRANTE1:</b>
<b>NOME:</b> <pre>{qsa}</pre>
<b>CARGO:</b> <pre>{qsa2}</pre>

<b>INTEGRANTE2:</b>
<b>NOME:</b> <pre>{qsa3}</pre>
<b>CARCO:</b> <pre>{qsa4}</pre>
<b>BY:</b> @ThiCrazyRoBOT""", "html", reply_to_message_id=msg["message_id"])
  except:
   bot.sendMessage(id2, "<b>CNPJ NÃO ENCONTRADO!</b>", "html", reply_to_message_id=msg["message_id"])

 if(text.upper() == "/ID"):
  bot.sendMessage(id2, f"""<b>DADOS ENCONTRADOS!!</b>

<b>NOME:</b> {id1}
<b>USER:</b> @{id3}
<b>ID:</b> {id2}
<b>LINGUAGEM:</b> {id4}
<b>BY:</b> @ThiCrazyRoBOT""", "html", reply_to_message_id=msg["message_id"])


MessageLoop(bot, main).run_as_thread()
print("\n" * 500)
print("R O D A N D O")
while True:
 pass
