print("Sistema de Briefing Teste do Guilherme Monteiro")
print("Seja bem-vindo(a)")



# Inputs principais
# A ideia é simples: coletar informações sobre o o briefing de jobs de um usuário e realizar o print do mesmo para o gestor do sistema
# Há como exportar os dados para uma planilha em excel e contabilizar, assim, os jobs do mês ou de um período específico?

#informações do usuário
def informacoes_usuario():

    nome = input("Informe o seu nome: ")
    setor = input("Qual é o seu setor? ")
    cargo = input("Qual é o seu cargo? ")


#informações do job
def informacoes_jobs():
    while True:

        job = input("Qual é o job a ser desenvolvido? \n 1 - Postagem em Redes Sociais \n 2 - Composição de Material Impresso \n 3 - Brindes ou Similares \n 4 - Video ou Motion \n 5 - Design Web \n 6 - Sair")


        if job == '1':
            lista_job_social = []
            job_social = job

            print("Preciso saber mais algumas informações para processar o seu briefing!")
            assunto_post = input("Qual é o assunto desta postagem? ")
            campanha_post = input("Esta postagem tem uma campanha definida? Qual? ")
            formato_post = input("Sua postagem será veiculada no feed, story ou em ambos? ")
            midia_post = input("Informe em quais redes sociais onde esta postagem será realizada: ")
            data_post = input("Informe a data em que essa postagem precisa ser veiculada (xx/xx/xxxx): ")
            confirme_post = print("Para confirmar. Sua postagem será sobre: {}, {}, {}, {}, {}".format(assunto_post, campanha_post, formato_post, midia_post, data_post))
            print("Obrigado, encaminharei estas informações ao responsável pelo Social Media do setor! :) ")

            lista_job_social.append(job_social)


        if job == '2':
            lista_job_impresso = []
            job_impresso = job

            print("Preciso saber mais algumas informações para processar o seu briefing!")
            tipo_impresso = input("Especifique o tipo de material impresso a ser desenvolvido (ex. cartão de visitas): ")
            campanha_impresso = input("Este material se relaciona a alguma campanha definida? Qual? ")
            evento_impresso = input("Este material se relaciona a algum evento institucional interno ou externo? Especifique (ex. feira xyz em y cidade): ")
            formato_impresso = input("Qual é o formato de seu material (ex. A4, A5, A6...: ")
            quantidade_impresso = input("Por favor, informe a quantidade necessária para esta impressão: ")
            data_impresso = input("Para quando você precisa destes materiais impressos (xx/xx/xxxx)? ")
            confirme_impresso = print("Para confirmar. Seu impresso será: {}, {}, {}, {}, {}".format(tipo_impresso, campanha_impresso,evento_impresso, formato_impresso, quantidade_impresso, data_impresso))
            print("Obrigado, encaminharei estas informações para o Designer Gráfico do setor! :) ")

            lista_job_impresso.append(job_impresso)

        if job == '3':
            lista_job_brindes = []
            job_brindes = job

            print("Preciso saber mais algumas informações para processar o seu briefing!")
            tipo_brinde = input("Qual é o tipo de seu brinde? (ex. caneca, chaveiro, caneta)  ")
            campanha_brinde = input("Este brinde se relaciona com alguma campanha definida? Qual? ")
            arte_brinde = input("Você tem uma arte desenvolvida para este brinde? ")
            link_brinde = input("Se sim, poste o link onde esta arte se encontra: ")
            data_brinde = input("Para quando este brinde precisa estar pronto? (xx/xx/xxxx): ")
            quantidade_brinde = input("Informe a quantidade necessária: ")
            confirme_brinde = print("Para confirmar. Seu brinde será: {}, {}, {}, {}, {}".format(tipo_brinde, campanha_brinde, arte_brinde, link_brinde, data_brinde, quantidade_brinde))
            print("Obrigado, encaminharei estas informações ao responsável pelo Design Gráfico do setor! :) ")

            lista_job_brindes.append(job_brindes)


        if job == '4':
            lista_job_video_motion = []
            job_video_motion = job

            print("Preciso saber mais algumas informações para processar o seu briefing!")
            tipo_video_motion = input("Você precisa de um vídeo ou motion? ")
            formato_video = input("Qual é o formato do seu vídeo (tela cheia, feed 1080x1080, story 1080x1920...) ")
            campanha_video = input("Este vídeo/motion se relaciona com alguma campanha definida? Qual? ")
            assunto_video = input("Qual é o assunto deste vídeo/motion? ")
            local_video = input("Em caso de vídeo: onde o seu vídeo será gravado? ")
            participantes_video = input("Em caso de vídeo: quem participará deste vídeo (entrevistado, etc)? ")
            filmagem_externa_video = input("Seu vídeo é uma gravação de ambiente externo? (S/N) ")
            abertura_video = input("Seu vídeo precisa de uma abertura especial? Descreva: ")
            motion_artes = input("Em caso de motion: você tem as artes para a produção do seu motion? (S/N) ")
            motion_artes_link = input("Se sim, poste aqui o link de suas artes: ")
            post_video = input("Em quais plataformas/redes sociais este vídeo será postado? ")
            data_video = input("Para quando este vídeo/motion precisa estar pronto? (xx/xx/xxxx): ")
            confirme_video = print("Para confirmar. Seu vídeo/motion será sobre: {}, {}, {}, {}, {}".format(tipo_video_motion, formato_video, campanha_video, assunto_video, local_video,participantes_video, filmagem_externa_video, abertura_video, motion_artes, motion_artes_link, post_video, data_video))
            print("Obrigado, encaminharei estas informações ao responsável pela Produção de Vídeos/Motions do setor! :) ")

            lista_job_video_motion.append(job_video_motion)


        if job == '5':
            lista_job_web = []
            job_web = job

            print("Preciso saber mais algumas informações para processar o seu briefing!")
            tipo_web = input("Qual é o tipo de desenvolvimento web que você precisa? (Blog, Landing Page, Site Institucional, E-Commerce...) ")
            campanha_web = input("Este dev/web se relaciona com alguma campanha definida? Qual? ")
            assunto_web = input("Descreva o assunto: ")
            linguagem_web = input("Seu dev/web será construído desevolvido em plataforma CMS (Wordpress + Elementor, etc) ou em linguagem dev/web (HTML, CSS, etc)? ")
            objetivo_web = input("Descreva o objetivo (captura de leads, vendas digitais, etc.): ")
            referencia_web = input("Indica alguma referência? Link: ")
            protitipo_web = input("Você já desenvolveu um protótipo UI&UX deste dev/web? Link: ")
            seo_web_keywords = input("Insira aqui algumas palavras-chaves para otimização SEO: ")
            arquivos_web_links = input("Insira aqui o link com o conteúdo armazenado em nuvem para o seu web/dev: ")
            data_web = input("Para quando você precisa deste dev/web? (xx/xx/xxxx) ")
            confirme_video = print("Para confirmar. Seu vídeo/motion será sobre: {}, {}, {}, {}, {}".format(tipo_web,campanha_web, assunto_web,objetivo_web, linguagem_web, referencia_web,protitipo_web, seo_web_keywords, arquivos_web_links, data_web))
            print("Obrigado, encaminharei estas informações ao responsável pela Produção de Vídeos/Motions do setor! :) ")

            lista_job_web.append(job_web)

        if job =='6':
            print("Até mais! :)")
            break


        servico = input("Precisa de algo mais? (S/N) ")
        if servico == 'S':
            continue
        else:
            print("Obrigado, em breve enviaremos mais informações sobre o seu Briefing :)")
            break



informacoes_usuario()
informacoes_jobs()



