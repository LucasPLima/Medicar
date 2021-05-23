import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NotificationService } from 'src/app/util/notification.service';
import { UserRegister } from '../user-register.model';
import { UserService } from '../user.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css'],
})
export class CreateComponent implements OnInit {
  
  userRegister: UserRegister = 
     {
       first_name:"lucas",
       last_name:"llluuuu",
       email:"lu@quinha.com",
       password:"123456",
       username:"luquinha"
     };

     createForm = new FormGroup(
      {
        first_name: new FormControl(this.userRegister.first_name,[Validators.required]),
        last_name: new FormControl(this.userRegister.last_name,[Validators.required]),
        email: new FormControl(this.userRegister.email,[Validators.required]),
        username: new FormControl(this.userRegister.username,[Validators.required]),
        password: new FormControl(this.userRegister.password,[Validators.required]),      
      }
    )

  hide = true;
  
  constructor(
    private router: Router,
    private userService: UserService,
    private notificationService: NotificationService
  ) { }

  ngOnInit(): void {
  
  }

  hidePassword():void{
    this.hide = !this.hide;
  }

  inputType(): string{
    return this.hide ? 'password' : 'text';
  }

  redirectToLogin():void{
    this.router.navigate(['login'])
  }

  createAccount(){
    this.userService.create(this.userRegister).subscribe(
      response => {
        console.log(response)
        this.notificationService.showSuccessMsg(`Usuário ${response.username} criado com sucesso.`)
        this.redirectToLogin()
      }
    )
  }
}
