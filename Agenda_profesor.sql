select p.id , p.nombre, c.materia ,c.dias,c.inicio,c.final,c.instituo,c.salon from profesores p left join clases c on p.id = c.id_profe;
select * from clases
