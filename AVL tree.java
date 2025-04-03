//Pavel Khramov
//Solution was discussed with Anna Meshcheriakova
package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Comparator<Integer> cmp = (i, j) -> i <= j;
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine().strip());
        AVLTree<Integer, Integer> avlTree = new AVLTree<>(-99999999, -1, cmp);
        avlTree.root.height = -1;
        for (int i = 0; i < n; i++) {
            String[] command = scanner.nextLine().strip().split(" ");
            try {
                if (command[0].equals("ADD")) {
                    avlTree.insert(avlTree.root, Integer.parseInt(command[1]), Integer.parseInt(command[2]));
                }
                else if (command[0].equals("LOOKUP")) {
                    System.out.println(avlTree.select(avlTree.root, Integer.parseInt(command[1])).value);
                }
                else if (command[0].equals("DELETE")) {
                    avlTree.delete(Integer.parseInt(command[1]));
                }
                else if (command[0].equals("PRINT_ROTATIONS")) {
                    System.out.println(avlTree.numberOfRotations);
                }
            } catch (RuntimeException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}

class AVLTree<K, V> {
    int numberOfRotations;
    Node<K, V> root;
    private Comparator<K> cmp;

    AVLTree(Comparator<K> cmp) {
        root = new Node<>(null);
    }
    AVLTree(K key, V value, Comparator<K> cmp) {
        numberOfRotations = 0;
        root = new Node<>(null, null, null, key, value);
        root.left = new Node<>(root);
        root.right = new Node<>(root);
        root.height = -1;
        this.cmp = cmp;
    }

    public Node<K, V> select(Node<K, V> node, K key) {
        if (node.key == key) return node;
        if (node.height == -1) throw new RuntimeException("KEY NOT FOUND");
        else {
            if (cmp.cmpr(key, node.key)) return select(node.left, key);
            else return select(node.right, key);
        }
    }

    public void delete(K key) {
        Node<K, V> nodeDel = select(root, key);
        if (nodeDel.left.height == -1 && nodeDel.right.height == -1) {
            deleteLeaf(nodeDel);
        } else if (nodeDel.left.height != -1 && nodeDel.right.height == -1) {
            deleteOneChLeft(nodeDel);
        } else if (nodeDel.left.height == -1 && nodeDel.right.height != -1) {
            deleteOneChRight(nodeDel);
        } else {
            Node<K, V> predeccessor = findPredeccessor(nodeDel.right);
            nodeDel.value = predeccessor.value;
            nodeDel.key = predeccessor.key;
            if (predeccessor.left.height == -1 && predeccessor.right.height == -1) deleteLeaf(predeccessor);
            else if (predeccessor.left.height != -1) deleteOneChLeft(predeccessor);
            else deleteOneChRight(predeccessor);
        }
    }
    private void deleteLeaf(Node<K, V> nodeDel) {
        if (nodeDel == root) {
            root.key = null;
            root.value = null;
            root.height = -1;
            root.parent = null;
            root.differFactor = 0;
        } else {
            Node<K, V> par = nodeDel.parent;
            if (par.left.key == nodeDel.key) par.left = new Node<>(nodeDel);
            else par.right = new Node<>(nodeDel);
            recountHeight(par);
        }
    }
    private void deleteOneChLeft(Node<K, V> nodeDel) {
        if (nodeDel == root) {
            root = nodeDel.left;
            root.parent = null;
            root.height = Math.max(root.left.height, root.right.height) + 1;
            root.differFactor = root.right.height - root.left.height;
        } else {
            nodeDel.left.parent = nodeDel.parent;
            if (nodeDel.parent.left.key == nodeDel.key) {
                nodeDel.parent.left = nodeDel.left;
            } else {
                nodeDel.parent.right = nodeDel.left;
            }
            recountHeight(nodeDel.parent);
        }
    }
    private void deleteOneChRight(Node<K, V> nodeDel) {
        if (nodeDel == root) {
            root = nodeDel.right;
            root.height = Math.max(root.left.height, root.right.height) + 1;
            root.differFactor = root.right.height - root.left.height;
        } else {
            nodeDel.right.parent = nodeDel.parent;
            if (nodeDel.parent.left.key == nodeDel.key) {
                nodeDel.parent.left = nodeDel.right;
            } else {
                nodeDel.parent.right = nodeDel.right;
            }
            recountHeight(nodeDel.parent);
        }
    }
    private Node<K, V> findSuccessor(Node<K, V> node) {
        if (node.right.height != -1) return findSuccessor(node.right);
        else return node;

    }
    private Node<K, V> findPredeccessor(Node<K, V> node) {
        if (node.left.height != -1) return findPredeccessor(node.left);
        else return node;
    }
    private void recountHeight(Node<K, V> node) {
        node.height = Math.max(node.left.height, node.right.height) + 1;
        node.differFactor = node.right.height - node.left.height;
        //checkForRotations(node);
        checkForRotations(node);
        if (node.key != root.key) {
            recountHeight(node.parent);
        }
    }

    public void insert(Node<K, V> node, K key, V value) {
        if (key == node.key) throw new RuntimeException("KEY ALREADY EXISTS");
        if (root.height == -1) {
            root = new Node<>(null, new Node<>(node), new Node<>(node), key, value);
            return;
        }

        //cmp <=
        if (cmp.cmpr(key, node.key)) {
            if (node.left.height == -1) {
                node.left = new Node<>(node, new Node<>(node.left), new Node<>(node.left), key, value);
            } else {
                insert(node.left, key, value);
            }
        } else {
            if (node.right.height == -1) {
                node.right = new Node<>(node, new Node<>(node.right), new Node<>(node.right), key, value);
            } else {
                insert(node.right, key, value);
            }
        }
        node.height = Math.max(node.left.height, node.right.height) + 1;
        node.differFactor = node.right.height - node.left.height;
        checkForRotations(node);
    }
    private void checkForRotations(Node<K, V> node) {
        if (node.differFactor == 2 && (node.right.differFactor == 1 || node.right.differFactor == 0)) leftRotation(node, node.right);
        else if (node.differFactor == -2 && (node.left.differFactor == -1 || node.left.differFactor == 0)) rightRotation(node, node.left);
        else if (node.differFactor == -2 && node.left.differFactor == 1) {

            leftRotation(node.left, node.left.right);
            rightRotation(node, node.left);

        } else if (node.differFactor == 2 && node.right.differFactor == -1) {

            rightRotation(node.right, node.right.left);
            leftRotation(node, node.right);

        }
    }
    private void leftRotation(Node<K, V> x, Node<K, V> y) {
        numberOfRotations++;
        if (x == root) root = y;
        y.parent = x.parent;
        x.right = y.left;
        y.left.parent = x;
        y.left = x;
        x.parent = y;
        if (y != root) {
            if (y.parent.right.key == x.key) y.parent.right = y;
            else y.parent.left = y;
        }
        x.height = Math.max(x.left.height, x.right.height) + 1;
        x.differFactor = x.right.height - x.left.height;
        y.height = Math.max(y.left.height, y.right.height) + 1;
        y.differFactor = y.right.height - y.left.height;
    }

    private void rightRotation(Node<K, V> y, Node<K, V> x) {
        numberOfRotations++;
        if (y == root) root = x;
        x.parent = y.parent;
        y.left = x.right;
        x.right.parent = y;
        x.right = y;
        y.parent = x;
        //y.parent.left = x;
        if (x != root) {
            if (x.parent.left.key == y.key) x.parent.left = x;
            else x.parent.right = x;
        }
        y.height = Math.max(y.left.height, y.right.height) + 1;
        y.differFactor = y.right.height - y.left.height;
        x.height = Math.max(x.left.height, x.right.height) + 1;
        x.differFactor = x.right.height - x.left.height;
    }

    public void printTree(Node<K, V> node, String name) {
        if (node.height != -1) {
            System.out.print(node.key + ":" + name + " " + node.height + " ");
            if (node.left.height != -1) printTree(node.left, "Left.Height");
            if (node.right.height != -1) printTree(node.right, "Right.Height");
        }
    }
}

class Node<K, V> {
    Node<K, V> parent;
    Node<K, V> right;
    Node<K, V> left;

    K key;
    V value;

    int height;
    int differFactor;

    Node(Node<K, V> parent) {
        this.parent = parent;
        this.height = -1;
        this.differFactor = 0;
    }

    Node(Node<K, V> parent, Node<K, V> left, Node<K, V> right, K key, V value) {
        this.parent = parent;
        this.left = left;
        this.right = right;
        this.value = value;
        this.key = key;
        this.height = 0;
        this.differFactor = 0;
    }
    Node(Node<K, V> parent, Node<K, V> left, Node<K, V> right, K key, V value, int height, int differFactor) {
        this(parent, left, right, key, value);
        this.height = height;
        this.differFactor = differFactor;
    }
}
@FunctionalInterface
interface Comparator<T> {
    boolean cmpr(T value1, T value2);
}