class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

  class AVL_Tree(object): 
   
    def insert(self, root, key): 
      
        # Passo 1 - Executar normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Passo 2 - Atualiza a altura do node pai

        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Passo 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Passo 4 - Se o Node for desbalanceado
        # fazer os 4 casos de teste
        # Case 1 - Esquerda Esquerda 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Direita Direita 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Esquerda Direita 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Direita Esquerda 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Realizar Rotação
        y.left = z 
        z.right = T2 
  
        # Atualizar altura da arvore
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # retorna a nova raiz
        return y 

        def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Realiza a rotação
        y.right = z 
        z.left = T3 
  
        # Atualiza a altura
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Retorna a raiz
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 