import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {

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

  redirectToLogin():void{
    this.router.navigate(['login'])
  }

}
