import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  hide = true;
  
  constructor(
    private router: Router
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
    this.router.navigate(['/register']);
  }
  
}
