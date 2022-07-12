SELECT
	gu.NOME ,
	SUM(fmc.TOT_NOTA_FISCAL) as TOTAL
FROM
	FAT_MOVIMENTO_CAPA fmc
LEFT JOIN FAT_TIPO_TRANSACAO ftt ON
	ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO
LEFT JOIN GER_USUARIO gu ON
	gu.USUARIO = fmc.USUARIO 
WHERE
	fmc.STATUS = 'F'
	AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M')
	AND ftt.TIPO = 'S'
	AND fmc.EMPRESA = 1
	AND fmc.REVENDA = 1
	AND fmc.TIPO_TRANSACAO = 'V21'
	AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('01/06/2021', 'dd/mm/yyyy') AND TO_DATE('30/06/2021', 'dd/mm/yyyy')
GROUP BY gu.NOME
ORDER BY TOTAL DESC
	
