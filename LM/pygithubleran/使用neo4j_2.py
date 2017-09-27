from py2neo import Graph, Node, Relationship

g = Graph("http://localhost:7474", username="neo4j", password="123456")


tx = g.begin()

alice = tx.merge_one("Person", name="alice")
bob = tx.merge_one("Person", name="bob")
tx.create_unique(Relationship(alice, "KNOWS", bob))



tx.commit()


