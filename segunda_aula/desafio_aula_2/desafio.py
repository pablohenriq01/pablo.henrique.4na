class LinearRegression:
    #Inicialização dos coeficientes da regressão linear.
    def __init__(self):
        #Coeficiente angular
        self.slope = 0
        #Coeficiente linear
        self.intercept = 0

    #Ajustar o modelo de regressão linear.
    def fit(self, X, y):
        n = len(X)
        sum_x = sum(X)
        sum_y = sum(y)
        sum_xy = sum(x * y for x, y in zip(X, y))
        sum_xx = sum(x * x for x in X)

        self.slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
        self.intercept = (sum_y - self.slope * sum_x) / n


    #Fazer previsões com o modelo de regressão linear.
    def predict(self, X):
        return [self.slope * x + self.intercept for x in X]


if __name__ == "__main__":
    #Exemplos de dados passados pelo professor.
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]


    # Criação do modelo
    model = LinearRegression()
    model.fit(x, y)

    # Previsões
    predictions = model.predict(x)
    print("Previsões:", predictions)
    print("Slope:", model.slope)
    print("Intercept:", model.intercept)