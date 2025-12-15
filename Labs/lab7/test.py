class FaceRegister:

    def __init__(self, Face, Neutral_Face, method="affine"):
        self.Face = Face
        self.Neutral_Face = Neutral_Face
        self.method = method.lower()
        self.coefficients = {}

    def normalize_data(self):
        self.Face = self.Face - np.mean(self.Face, axis=0)
        self.Neutral_Face = self.Neutral_Face - \
            np.mean(self.Neutral_Face, axis=0)

        # Scale the data to unit variance (L2-norm scaling)
        self.Face = self.Face / np.linalg.norm(self.Face, axis=0)
        self.Neutral_Face = self.Neutral_Face / \
            np.linalg.norm(self.Neutral_Face, axis=0)

    def extract_columns(self):
        self.x_i_prime = self.Face[:, 0]
        self.y_i_prime = self.Face[:, 1]
        self.x_i = self.Neutral_Face[:, 0]
        self.y_i = self.Neutral_Face[:, 1]

    def compute_affine_coefficients(self):
        self.coefficients = {
            'A': np.sum(self.x_i_prime**2),
            'B': np.sum(self.x_i_prime * self.y_i_prime),
            'C': np.sum(self.y_i_prime**2),
            'D': np.sum(self.x_i_prime * self.x_i),
            'E': np.sum(self.y_i_prime * self.x_i),
            'F': np.sum(self.x_i_prime * self.y_i),
            'G': np.sum(self.y_i_prime * self.y_i),
        }

    def compute_similarity_coefficients(self):
        self.coefficients = {
            'A': np.sum(self.x_i_prime**2 + self.y_i_prime**2),
            'B': np.sum(-2 * (self.x_i_prime * self.y_i_prime)),
            'C': np.sum(self.x_i * self.x_i_prime + self.y_i * self.y_i_prime),
            'D': np.sum(self.y_i * self.x_i_prime - self.x_i * self.y_i_prime),
        }

    def construct_affine_matrices(self):
        A, B, C = self.coefficients['A'], self.coefficients['B'], self.coefficients['C']
        D, E, F, G = self.coefficients['D'], self.coefficients['E'], self.coefficients['F'], self.coefficients['G']
        coeff_matrix = np.array([[A, B, 0, 0],
                                 [B, C, 0, 0],
                                 [0, 0, A, B],
                                 [0, 0, B, C]])
        constants = np.array([D, E, F, G])
        return coeff_matrix, constants

    def construct_similarity_matrices(self):
        A, B = self.coefficients['A'], self.coefficients['B']
        C, D = self.coefficients['C'], self.coefficients['D']
        coeff_matrix = np.array([[A, 0], [B, A]])
        constants = np.array([C, D])
        return coeff_matrix, constants

    def solve_linear_system(self):
        if self.method == "affine":
            coeff_matrix, constants = self.construct_affine_matrices()
        elif self.method == "similarity":
            coeff_matrix, constants = self.construct_similarity_matrices()
        else:
            raise ValueError("Invalid method. Use 'affine' or 'similarity'.")
        solution = np.linalg.solve(coeff_matrix, constants)
        return solution

    def register(self):
        self.normalize_data()
        self.extract_columns()
        if self.method == "affine":
            self.compute_affine_coefficients()
        elif self.method == "similarity":
            self.compute_similarity_coefficients()
        else:
            raise ValueError("Invalid method. Use 'affine' or 'similarity'.")
        solution = self.solve_linear_system()
        if self.method == "affine":
            a, b, c, d = solution
            return np.array([[a, b], [c, d]])
        elif self.method == "similarity":
            a, b = solution
            return np.array([[a, -b], [b, a]])
