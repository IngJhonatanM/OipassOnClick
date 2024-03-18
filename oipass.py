import json_manager
import click
from passlib.context import CryptContext

@click.group
def oipass():
    pass


#Define password context 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    pwd = pwd_context.hash(password)
    return pwd

#Function and decorator for create new users & Password Encrypt

@oipass.command()
@click.option('--Account', required=True, help="Account' name")
@click.option('--Password', required=True, help="Password' Account")
@click.pass_context
def NewAccount(ctx, account, password):
    if not account or not password:
        ctx.fail('the account and password are required')
    elif password == type(str):
        pass
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        nuevo_registro = {'id': new_id, 'name': account, 'lastname': hash_password(password)}
        data.append(nuevo_registro)
        json_manager.write_json(data)
        print(f"new account created with id : {new_id}",'\n' 'name:', account,'\n''with hash:', nuevo_registro['lastname'])
    
#Function and decorator for show you users

@oipass.command()
def Accounts():
   users = json_manager.read_json()
   for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")
        
#Verify password

def verify_password(password, hashpassword):
    result = pwd_context.verify(password,hashpassword)
    if result:
        return "password correct"
    return "password incorrect"

#Function and decorator for show you user specific in id

@oipass.command()
@click.argument('id', type=int)
@click.argument('password')
def user(id, password):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    hash_password(password) == user['lastname']
    if user is None:
        print('User with id {id} not found')
    else:
         print(f"{user['id']} - {user['name']} -{user['lastname']}", verify_password(password,  user['lastname']))
        
#Function and decorator for delete user

@oipass.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print('user not found')
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id {id} deleted successfully")

#Function and decorator for update user

@oipass.command()
@click.argument('id', type=int)
@click.option('--name', default=None)
@click.option('--password', default=None)
def update(id, name, password):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if password is not None:
                user['lastname'] = hash_password(password)
            break
    json_manager.write_json(data)
    print(f"User with id {id} updated successfully")
    

if __name__ == '__main__':
    oipass()