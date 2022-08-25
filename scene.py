from manim import *


class LabeledModifiedGraph(Scene):
  def change_queue(self, graph, l):
    l = '\n'.join(l)
    queue2 = Text(f'Queue:\n{l}', font_size=24)
    queue2.next_to(graph, RIGHT)
    queue2.shift(2 * UP)
    self.play(ApplyMethod(self.queue.become, queue2))
    self.wait(0.1)

  def change_paths(self, graph, text):
    paths2 = Text('Paths:\n' + text, font_size=24)
    paths2.next_to(graph, RIGHT)
    paths2.shift(DOWN)
    self.play(ApplyMethod(self.paths.become, paths2))
    self.wait(0.1)

  def construct(self):
    vertices = ['S', 2, 3, 4, 5, 6, 7, 'E']
    edges = [
        ('S', 2), ('S', 4),
        (2, 3), (2, 7), (2, 'E'),
        (3, 4), (3, 5), (3, 6), (3, 7), (3, 'E'),
        (5, 'E'),
        (6, 7), (6, 'E'),
    ]

    graph = Graph(
        vertices,
        edges,
        layout_scale=2.5,
        labels=True,
        vertex_config={
            'S': {'fill_color': RED},
            2: {'fill_color': RED},
            'E': {'fill_color': RED},
        },
        edge_config={
            ('S', 2): {'stroke_color': RED},
            (2, 'E'): {'stroke_color': RED},
        }
    )

    self.add(graph)

    self.wait(1)

    graph.generate_target()
    graph.target.move_to(3*LEFT)
    self.play(MoveToTarget(graph))

    self.wait(1)

    title1 = Text('Fixed length search')
    title1.to_edge(UP)

    self.play(Write(title1))

    self.wait(0.5)

    title2 = Text('Fixed (5) length search')
    title2.to_edge(UP)

    self.play(Transform(title1, title2))

    distances = Text(
        '''Distances to S:
2 - 1
3 - 2
4 - 1
5 - 3
6 - 3
7 - 3
E - 2''', font_size=24)
    distances.shift(UP + 1.5 * RIGHT)
    self.play(Write(distances))

    self.wait(2)

    predecessors = Text(
        '''Precessors from the start:
S ⟶ 2
2 ⟶ 3
S ⟶ 4
3 ⟶ 5
3 ⟶ 6
2 ⟶ 7
2 ⟶ E
''', font_size=24)
    predecessors.next_to(distances, DOWN)
    predecessors.shift(0.9 * RIGHT)
    self.play(Write(predecessors))

    self.wait(2)

    self.play(Uncreate(distances))
    self.play(Uncreate(predecessors))

    self.queue = Text('Queue:\nS', font_size=24)
    self.queue.next_to(graph, RIGHT)
    self.queue.shift(2 * UP)
    self.play(Write(self.queue))

    self.wait(1)

    self.paths = Text('Paths:\nS ⟶ 2', font_size=24)
    self.paths.next_to(graph, RIGHT)
    self.paths.shift(DOWN)
    self.play(Write(self.paths))

    self.change_queue(graph, ['S', '2'])
    self.change_paths(graph, 'S ⟶ 2\nS ⟶ 4')
    self.change_queue(graph, ['S', '2', '4'])
    self.change_queue(graph, ['2', '4'])
    self.change_paths(graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3')
    self.change_queue(graph, ['2', '4', '3'])
    self.change_paths(graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 7')
    self.change_queue(graph, ['2', '4', '3', '7'])
    self.change_paths(graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 7\nS ⟶ 2 ⟶ E')
    self.change_queue(graph, ['4', '3', '7'])
    self.change_queue(graph, ['3', '7'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 7\nS ⟶ 2 ⟶ E')
    self.change_queue(graph, ['3', '7', '5'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 6\nS ⟶ 2 ⟶ 7\nS ⟶ 2 ⟶ E')
    self.change_queue(graph, ['3', '7', '5', '6'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 6\nS ⟶ 2 ⟶ 3 ⟶ 7\nS ⟶ 2 ⟶ E')
    self.change_queue(graph, ['3', '7', '5', '6', '7'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 6\nS ⟶ 2 ⟶ 3 ⟶ 7\nS ⟶ 2 ⟶ 3 ⟶ E')
    self.change_queue(graph, ['7', '5', '6', '7'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 7 ⟶ 6\nS ⟶ 2 ⟶ 3 ⟶ 7\nS ⟶ 2 ⟶ 3 ⟶ E')
    self.change_queue(graph, ['5', '6', '7'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 7 ⟶ 6\nS ⟶ 2 ⟶ 3 ⟶ 7\nS ⟶ 2 ⟶ 3 ⟶ 5 ⟶ E')
    self.change_queue(graph, ['6', '7'])
    self.change_paths(
        graph, 'S ⟶ 2\nS ⟶ 4\nS ⟶ 2 ⟶ 3\nS ⟶ 2 ⟶ 3 ⟶ 5\nS ⟶ 2 ⟶ 3 ⟶ 7 ⟶ 6\nS ⟶ 2 ⟶ 3 ⟶ 7\nS ⟶ 2 ⟶ 3 ⟶ 7 ⟶ 6 ⟶ E')

    self.wait(1)

    graph2 = Graph(
        vertices,
        edges,
        layout_scale=2.5,
        labels=True,
        vertex_config={
            'S': {'fill_color': RED},
            2: {'fill_color': RED},
            3: {'fill_color': RED},
            7: {'fill_color': RED},
            6: {'fill_color': RED},
            'E': {'fill_color': RED},
        },
        edge_config={
            ('S', 2): {'stroke_color': RED},
            (2, 3): {'stroke_color': RED},
            (3, 7): {'stroke_color': RED},
            (7, 6): {'stroke_color': RED},
            (6, 'E'): {'stroke_color': RED},
        }
    )

    graph2.shift(3*LEFT)

    self.play(ReplacementTransform(graph, graph2))

    self.wait(2)
