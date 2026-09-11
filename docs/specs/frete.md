## REQ-01: Cálculo de Frete com Percentual
*RF-01* *WHEN* o cliente solicitar o cálculo de frete, *THE SYSTEM SHALL* aplicar o percentual configurado sobre o valor total do pedido para definir a taxa de entrega.

## REQ-02: Garantia de Valor Mínimo
*RF-02* *WHEN* o cálculo do frete resultar em um valor inferior ao limite mínimo estipulado, *THE SYSTEM SHALL* ajustar o valor final do frete para o valor mínimo configurado em R$.

## REQ-03: Tempo Limite de Resposta (Timeout)
*RF-03* *WHEN* a requisição de cálculo de frete exceder o tempo limite configurado em milissegundos (ms), *THE SYSTEM SHALL* interromper a tentativa e exibir uma mensagem de erro de conexão ao usuário.

# Especificação EARS - Parâmetros do Sistema

*RF-04*: WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete.

*RB-01*: WHILE a região for 'Norte', o limite é R$ 300,00. Demais regiões: R$ 200,00.

*RB-03*: IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'.