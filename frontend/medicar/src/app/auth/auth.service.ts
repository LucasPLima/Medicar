import { Injectable } from '@angular/core';
import { UserAuth } from '../components/user/user-auth.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private userInfo: UserAuth = {
    name: "Lucas Lima",
    token:"0de0251f16b69509ff1f57015d85d1b45e07d611"
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
