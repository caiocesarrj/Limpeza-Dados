select count(*) as total_pedidos from pedidos; -- Total de pedidos

select status, count(*) as quantidade
from pedidos
group by status
order by quantidade desc; -- Total de pedidos separados por categorias

select
	round(sum(preco_unitario * quantidade * (1 - coalesce(desconto, 0))), 2) as receita_total
from pedidos
where status = 'ENTREGUE'; -- Receita por pedidos entregues

select
	produto,
    sum(quantidade) as unidades_vendidas,
    round(sum(preco_unitario * quantidade * (1 - coalesce(desconto, 0))), 2) as receita
from pedidos
where status = 'ENTREGUE'
group by produto
order by receita desc
limit 5; -- Top 5 de produtos mais vendidos

select
	date_format(data_pedido, '%Y-%m') as mes,
    count(*) as total_pedidos,
    round(sum(preco_unitario * quantidade * (1 - coalesce(desconto, 0))), 2) as receita
from pedidos
where status = 'ENTREGUE'
	and data_pedido is not null
group by mes
order by mes; -- Evolução mensal dos pedidos


select status, count(*) as qtd
from pedidos
where date_format(data_pedido, '%Y-%m') = '2023-06'
group by status; -- Analisando motivo da queda de Junho de 2023 (230.000 para 18.000)