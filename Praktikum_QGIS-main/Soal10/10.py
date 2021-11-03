import shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("pratt","satu")
w.record("pritt","dua")
w.record("prutt","tiga")
w.record("prett","empat")
w.record("prott","lima")
w.record("tuttt","enam")

w.poly([[[3,1], [5,3], [3,5], [1,3], [3,1]]])
w.poly([[[9,1], [11,3], [9,5], [7,3], [9,1]]])

w.poly([[[15,1], [17,3], [15,5], [13,3], [15,1]]])
w.poly([[[3,6], [5,8], [3,10], [1,8], [3,6]]])

w.poly([[[9,6], [11,8], [9,10], [7,8], [9,6]]])
w.poly([[[15,6], [17,8], [15,10], [13,8], [15,6]]])


w.close()