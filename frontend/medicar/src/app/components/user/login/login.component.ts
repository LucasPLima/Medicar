import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth/auth.service';
import { NotificationService } from 'src/app/util/notification.service';
import { UserAuth } from '../user-auth.model';
import { UserLogin } from '../user-login.model';
import { UserService } from '../user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public userLogin: UserLogin =
  {
    username:'luquinha7',
    password:'123456'
  }

  hide = true;
  
  constructor(
    private router: Router,
    private userService: UserService,
    private notificationService: NotificationService,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
  }

  hidePassword():void{
    this.hide = !this.hide;
  }

  inputType(): string{
    return this.hide ? 'password' : 'text';
  }

  redirectToRegister():void{
    this.router.navigate(['/registrar']);
  }

  redirectToConsultas():void{
    this.router.navigate(['/consultas']);
  }

  login(){
    console.log(this.userLogin)
    this.userService.login(this.userLogin).subscribe(
      response => {
        this.authService.setUserInfo(response)
        this.notificationService.showSuccessMsg(`Bem vindo(a) ${response.name}.`)
        this.redirectToConsultas()
      }
    )
  }
  
}
