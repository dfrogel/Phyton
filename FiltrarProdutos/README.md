
# <img src="https://media.tenor.com/0l119tZ7yBcAAAAC/magalu-magazine-luiza.gif" alt="gif animado" width="80" height="auto"> Magalu Scraper

Este script utilizando a linguagem Python realiza a leitura e a impressão das informações (nome e valor) dos 6 primeiros produtos exibidos na página web: [Magalu - Ofertas do Dia](https://www.magazineluiza.com.br/selecao/ofertasdodia/)

## Descrição 

O Magalu Scraper é uma ferramenta simples e automatizada que coleta os dados dos 6 primeiros produtos exibidos na página "Ofertas do Dia" do Magazine Luiza. Utilizando as bibliotecas **requests** e **BeautifulSoup4**, o script acessa a página web, extrai as informações relevantes e as apresenta de forma organizada no console.

## Dependências

Para utilizar o Magalu Scraper, é necessário ter as seguintes bibliotecas instaladas:

- `requests`
- `BeautifulSoup4`

Caso ainda não tenha essas bibliotecas instaladas, você pode instalá-las usando o seguinte comando:

```bash
pip install requests beautifulsoup4
```

## Como usar

1. Clone este repositório ou copie o conteúdo do script `product.py`.
2. Certifique-se de que as dependências `requests` e `BeautifulSoup4` estão instaladas.
3. No diretório onde está localizado o script `product.py`, abra o terminal ou prompt de comando.
4. Execute o seguinte comando:
```bash
python product.py
```

## Exemplo de saída
```bash
Ofertas do dia (6 primeiros produtos) - MAGALU:

1. Produto: Pneu Aro 13 175/70R13 Goodyear 82T Touring
   Valor: R$ 299,90

2. Produto: Pneu Aro 13 Westlake 175/75R13PR 85T
   Valor: R$ 218,41

3. Produto: Escova Secadora Mondial Juliette 1200W - Cerâmica
   Valor: R$ 174,50

4. Produto: Escova Secadora Mondial Black Rose Argan ES-14 - 1200W Cerâmica com Íons 3 Velocidades
   Valor: R$ 106,60

5. Produto: Sabão em Pó Brilhante Cuidado Total - Roupas Brancas e Coloridas Original 1,6kg
   Valor: R$ 21,99

6. Produto: Forno Elétrico de Bancada Britânia com Dourador - 40L Preto BFE45PI
   Valor: R$ 408,49
```

## Atenção!!!
O funcionamento deste script depende da estrutura da página web do Magazine Luiza. 
Caso ocorram alterações na estrutura da página, como mudanças nas classes dos elementos HTML que estamos buscando, o script precisará ser atualizado para refletir essas mudanças e continuar funcionando corretamente.

## Aviso
Este script foi criado apenas para fins educacionais e de aprendizado. Respeite sempre os termos de serviço e a política de uso dos sites ao realizar scraping.

## Autor
Eduarda Frogel 👩🏻‍💻

dudafrogel23@gmail.com 📩

Obrigada por chegar até aqui! Em caso de dúvidas não hesite em entrar em contato. 😉


