def add_contact(contacts, name, email):
    contact=(name, email)
    contacts.append(contact)
    print(f"Contacto {name} agregado!")
    return contacts

def show_contacts(contacts):
    print("---------------------------------")
    if contacts: 
        print("Lista de contactos:")
        for name,email in contacts:
            print(f"Nombre: {name}, email: {email}")
    else:
        print("No hay contactos en la lista")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            print(f"Contacto {name} eliminado!")
            return contacts
    print(f"No existe el contacto {name} en la lista")
    return contacts

print("Valor de __name__: ", __name__)
print()
if __name__ == "__main__":
    contacts = []
    contacts = add_contact(contacts, "matias", "matiasdelapuente@yahoo.com.ar")
    contacts = add_contact(contacts, "mauri", "toledomauricioj@gmail.com")   
    show_contacts(contacts)
    contacts = delete_contact(contacts, "matias")
    show_contacts(contacts)