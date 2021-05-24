import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from 'src/app/auth/auth.service';
import { UserAuth } from './user-auth.model';
import { UserLogin } from './user-login.model';
import { environment } from '../../../environments/environment';
import { EMPTY, Observable } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import { UserRegister } from './user-register.model';
import { NotificationService } from 'src/app/util/notification.service';
import { MatSnackBar } from '@angular/material/snack-bar';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient,
              private authService: AuthService,
              private notificationService: NotificationService,
              private snackBar: MatSnackBar
              ) { }


  errorHandler(e:any):Observable<any>{
    const status = e.status.toString()
    
    if (status.charAt(0)==='4'){
      const responseError = e.error
      const errorObject = Object.keys(responseError)[0]
      const messageError= responseError[errorObject][0]
      this.notificationService.showWarningMsg(`${messageError} (${errorObject})`)
    }else{
      this.notificationService.showErrorMsg("Erro de comunicação com o servidor.")
    }
    
    return EMPTY;
  }
  
  login(userCredentials:UserLogin): Observable<UserAuth>{
    return this.http.post<UserAuth>(`${environment.apiURL}/login/`, userCredentials).pipe(
      map((obj)=> obj),
      catchError((e)=>this.errorHandler(e))
    )
  }

  create(userInfo: UserRegister): Observable<any>{
    return this.http.post<any>(`${environment.apiURL}/registrar/`, userInfo).pipe(
      map((obj)=> obj),
      catchError((e)=>this.errorHandler(e))
    )
  }

  logout(){
    this.authService.setUserInfo({token:"", name:""})
  }

}
