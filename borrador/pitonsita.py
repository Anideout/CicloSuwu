from random import randint

products = [
 'Televisor',
 'Lavadora',
 'Refrigerador',
 'Microondas',
 'Computadora',
 'Celular',
 'Impresora',
 'Cafetera',
 'Licuadora',
 'Ventilador'
]

prices = []

def generate_prices():
  random_prices = []
  for product in products:
    random_prices.append([randint(300000, 2500000), product])
  return random_prices

def group_products_by_price(products):
  groups = [[], [], []]
  for product in products:
    price = product[0]
    if(price < 800000):
      groups[0].append(product[1])

    elif(price >= 800000 and price <= 2000000):
      groups[1].append(product[1])
      
    elif(price > 2000000):
      groups[2].append(product[1])
  return groups

def get_stats(products_list):
  products_list.sort()
  print(f'Producto más barato: {products_list[0][1]} - ${products_list[0][0]}')
  print(f'Producto más caro: {products_list[-1][1]} - ${products_list[-1][0]}')

  product_prices = []
  for product in products_list:
    product_prices.append(product[0])
  print(f'Promedio de precios {sum(product_prices)/len(product_prices)}')

  base_product = 1
  n = len(product_prices)

  for n in product_prices:
    base_product *= n
  print(f'La media geométrica es: {base_product ** (1/n)}')

def generate_report(products_list):
  file_name = f'REPORTE_PRECIOS'
  file = open(f'./{file_name}.csv', 'w')
  headers = [
    'PRODUCTO',
    'PRECIO_BASE',
    'PROMOCION_10%',
    'TOTAL_PROMOCION_10%',
    'MEMBRESIA_5%',
    'TOTAL_MEMBRESIA_5%'
  ]
  file.write('|'.join(headers)+'\n')
  for product in products_list:
    file.write(
      '|'.join([
        str(product[1]),
        str(product[0]),
        str(int(product[0] * 0.1)),
        str(int(product[0] - (product[0] * 0.1))),
        str(int(product[0] * 0.05)),
        str(int(product[0] - (product[0] * 0.05))),
      ])+'\n'
    )
  file.close()
  print(f'reporte generado: {file_name}.csv')

while True:
  # * Menu
  print('1.    Asignar precios aleatorios')
  print('2.    Clasificar precios')
  print('3.    Ver estadísticas')
  print('4.    Reporte de precios')
  print('5.    Salir del programa')
  option = int(input('\nIngrese una opción: '))

  # * Options
  if(option == 1):
    prices = generate_prices()

  elif(option == 2):
    groups = group_products_by_price(prices)
    print(groups)

  elif(option == 3):
    sort = get_stats(prices)

  elif(option == 4):
    generate_report(prices)
  
  elif(option == 5):
    print('xao bieja piruja')
    break