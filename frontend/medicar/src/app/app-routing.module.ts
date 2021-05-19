import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateComponent } from './components/user/create/create.component';
import { LoginComponent } from './components/user/login/login.component';

const routes: Routes = [
  {
    path:"login",
    component: LoginComponent
  },
  {
    path:"register",
    component: CreateComponent
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
