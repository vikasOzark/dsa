package main

import (
	"container/list"
	"fmt"
)

type GraphType[T comparable] map[T][]T

func main() {
	graph := GraphType[int]{
		0: {8, 1, 5},
		1: {0},
		5: {0, 8},
		8: {0, 5},
		2: {3, 4},
		3: {2, 4},
		4: {3, 2},
	}

	res := connectedComponentCount(graph)
	fmt.Println("connected count : ", res)
}

func graphDepthFirst(graph GraphType[string], source string) {
	stack := list.New()
	stack.PushBack(source)

	for stack.Len() > 0 {
		element := stack.Back()
		stack.Remove(element)
		current := element.Value.(string)
		println("=> ", current)

		graphValues := graph[current]
		for j := range graphValues {
			stack.PushBack(graphValues[j])
		}
	}
}

func hasPath(graph GraphType[string], src string, destination string) bool {
	stack := list.New()
	stack.PushBack(src)

	for stack.Len() > 0 {
		elememt := stack.Back()
		stack.Remove(elememt)
		current := elememt.Value.(string)

		if current == destination {
			return true
		}

		for j := range graph[current] {
			stack.PushBack(graph[current][j])
		}
	}

	return false
}

func buildGraphAdjancyList() GraphType[string] {
	data := [][]string{
		{"i", "j"},
		{"k", "i"},
		{"m", "k"},
		{"k", "l"},
		{"o", "n"},
	}

	adjancyList := GraphType[string]{}

	for i := range data {
		a, b := data[i][0], data[i][1]

		if adjancyList[a] == nil {
			adjancyList[a] = make([]string, 0)
		}

		if adjancyList[b] == nil {
			adjancyList[b] = make([]string, 0)
		}

		adjancyList[a] = append(adjancyList[a], b)
		adjancyList[b] = append(adjancyList[b], a)

	}
	return adjancyList
}

func hasPath_(graph GraphType[string], src string, dest string, visited *Set[string]) bool {

	if src == dest {
		return true
	}

	if visited.In(src) {
		return false
	}

	visited.Add(src)

	for i := range graph[src] {
		if hasPath_(graph, graph[src][i], dest, visited) {
			return true
		}
	}
	return false
}

func undirectedGraph() {
	graph := buildGraphAdjancyList()
	visited := NewSet[string]()
	println("Path exists:", hasPath_(graph, "i", "l", visited))
}

func connectedComponentCount(graph GraphType[int]) int {
	visited := NewSet[int]()
	count := 0
	for node := range graph {
		if explore(graph, node, visited) {
			count++
		}
	}

	return count
}

func explore(graph GraphType[int], current int, visited *Set[int]) bool {
	if visited.In(current) {
		return false
	}

	visited.Add(current)
	for _, d := range graph[current] {
		explore(graph, d, visited)
	}
	return true
}

func largestComponent(GraphType[int]) {

}

// Set data structure implimentation code
type Set[T comparable] struct {
	data map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
	return &Set[T]{data: make(map[T]struct{})}
}

func (s *Set[T]) Add(value T) {
	s.data[value] = struct{}{}
}

func (s *Set[T]) Remove(value T) {
	delete(s.data, value)
}

func (s *Set[T]) In(value T) bool {
	_, exists := s.data[value]
	return exists
}

func (s *Set[T]) Values() []T {
	keys := make([]T, 0, len(s.data))
	for key := range s.data {
		keys = append(keys, key)
	}
	return keys
}

func (s *Set[T]) Size() int {
	return len(s.data)
}
