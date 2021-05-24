import { Injectable } from '@angular/core';
import { UserAuth } from '../components/user/user-auth.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private userInfo: UserAuth = {
    name: "",
    token:""
  };

  constructor() { 

  }

  setUserInfo(userInfo:UserAuth){
    this.userInfo = userInfo
  }

  getUserName():string{
    return this.userInfo.name
  }

  getToken(): String {
    return this.userInfo.token
  }

  isAuthenticated(): boolean{
    if (this.userInfo.token.length === 0)
      return false
    return true
  }
}
