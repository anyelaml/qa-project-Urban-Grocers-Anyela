import sender_stand_request
import data


def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()  # Cuerpo actual es una copia del user body en data
    current_body["name"] = name  # Se cambia el valor del parámetro firstName
    # Se devuelve un nuevo diccionario con el valor firstName requerido (nuevo valor de first name)
    return current_body


# Pruebas positivas
def positive_assert(name):
    user_kit = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(user_kit)
    assert response.status_code == 201
    print(response.json())


# Prueba negativa
def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


# Prueba1, el parametro kit name tiene 1 caracter
def test_create_user_kit_1_letter_kit_body():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# Prueba 2, kit name con 511 caracteres
def test_create_user_kit_511_letter_kit_body():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                            bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                            abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                            bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                            dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdab\
                            cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                            cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                            abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                            abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)


# Prueba 3, kit name con 0 caracteres NEGATIVA
def test_create_user_kit_0_letter_kit_body():
    kit_body = get_kit_body("")
    negative_assert_400(kit_body)


# Prueba 4, 512 caracteres NEGATIVA

def test_create_user_kit_512_letter_kit_body():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
            bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
            dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
            dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
            abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
            cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_400(kit_body)


# Prueba 5, usando caracteres especiales

def test_create_user_kit_special_letter_kit_body():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)


# Prueba 6, espacios permitidos

def test_create_user_kit_blank_spaces_kit_body():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# Prueba 7, se permiten números

def test_create_user_kit_numbers_kit_body():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)


# Prueba 8, no hay parametro en la solicitud

def test_create_user_kit_no_parameter_kit_body():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_400(kit_body)


# Prueba 9, parametro different
def test_create_user_kit_different_parameter_kit_body():
    kit_body = get_kit_body(123)
    negative_assert_400(kit_body)
