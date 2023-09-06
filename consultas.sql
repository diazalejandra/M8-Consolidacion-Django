-- Se requiere un reporte que entregue la cantidad de órdenes por ciudad.
select	  address.city, 
		  count(salesorderheader.salesorderid) as cantidad_ordenes 
from 	  address
left join salesorderheader on address.addressid = salesorderheader.shiptoaddressid
group by  address.city;

-- Generar un listado de los clientes que son persona natural (tienen personid definido y storeid en null).
select 	  customerid, 
		  personid, 
		  storeid, 
		  territoryid 
from 	  customer
where 	  personid is not null 
		  and storeid is null;

-- Se necesita un reporte que muestre la cantidad de órdenes por territorio
select 	  salesterritory.name, 
		  count(salesorderheader.salesorderid) as cantidad_clientes 
from 	  salesterritory
left join salesorderheader on salesterritory.territoryid = salesorderheader.territoryid
group by  salesterritory.name, salesterritory.group, salesterritory.countryregioncode
order by  salesterritory.group desc, salesterritory.countryregioncode desc;