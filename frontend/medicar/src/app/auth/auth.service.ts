import { Injectable } from '@angular/core';
import { UserAuth } from '../components/user/user-auth.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor() { 
  }

  setUserInfo(userInfo:UserAuth){
    localStorage.setItem('name',userInfo.name)
    localStorage.setItem('token', userInfo.token)
    
  }

  getUserName():string{
    const name = localStorage.getItem('name')
    return name!==null? name : ''
  }

  getToken(): String {
    const token = localStorage.getItem('token')
    return token!==null? token : ''
  }

  logout():void{
    localStorage.clear()
  }

  isAuthenticated(): boolean{
    if (localStorage.getItem('token') !== null)
      return true
    return false
  }
}
